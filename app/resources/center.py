import os
import requests
import json
from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from werkzeug import secure_filename
from app.db import base
from app.helpers.auth import authenticated
from app.models.center import Center
from app.models.pageSetting import PageSetting
from app.helpers.permissions import *

# Protected resources
@permission_required('center_index')
def index():
    """Retorna una lista con el total de centros 
    """
    num_page = int(request.args.get('num_page', 1))
    quantity = PageSetting.find_settings()
    centers = base.session.query(Center).paginate(
        per_page=quantity.elements, page=num_page, error_out=True)
    num_pages = centers.iter_pages(
        left_edge=2, left_current=2, right_current=2, right_edge=2) 
    params = []
    params.append(centers)
    params.append(num_pages)
    return render_template("center/centros.html", centers=params[0], pages=params[1])

def search():
    """Realiza la búsqueda sobre usuarios por nombre de usuario o si 
    los mismos están activos o bloqueados y retorna el resultado de 
    forma paginada.
    """
    
    params = request.form.get('name')
    num_page = int(request.args.get('num_page', 1))
    quantity = PageSetting.find_settings()
    if params == '':
            centers = base.session.query(Center).paginate(per_page=quantity.elements, page=1, error_out=True)
    elif params == None:
        params=request.args.get('search')
        centers = base.session.query(Center).filter(Center.name.like("%" + params + "%")).paginate(per_page=quantity.elements, page=num_page, error_out=True)
    else: 
        centers = base.session.query(Center).filter(Center.name.like("%" + params + "%")).paginate(per_page=quantity.elements, page=num_page, error_out=True)
    num_pages = centers.iter_pages(left_edge=2, left_current=2, right_current=2, right_edge=2)
    return render_template("center/centros.html", centers=centers, pages=num_pages, search=params)


@permission_required('center_new')
def new():
    return render_template("center/new.html")


def create():
    """Crea un Centro con los valores recibidos.
    """
    params = request.form
    if request.method == 'POST':
        f = request.files['protocol'] 
        if f.filename != '':
            if f.filename.rsplit('.', 1)[1].lower() == 'pdf':
                parametros = params.to_dict()
                parametros['protocol'] = secure_filename(f.filename)
                mensaje = Center.create(parametros)
                filename = 'centro' + str(mensaje[1])
                f.save(os.path.join('app/static/uploads', filename + '.pdf'))
            else:
                flash('Formato de archivo incorrecto, el protocolo debe ser de tipo pdf', 'danger')
                return redirect(url_for("center_new"))
        else:
            mensaje = Center.create(params)
    flash(mensaje[0][0], mensaje[0][1])
    return redirect(url_for("centers"))

@permission_required('center_destroy')
def delete(idcenter):
    """Chequea que exista el centro con el id recibido por parámetro y 
    es redirigido a la pantalla para eliminar a un centro"""  
    center = Center.find_by_id(idcenter)
    return render_template("center/delete.html", center=center)

def commit_delete():
    """Llama a la función que realiza el borrado fisico de un centro y
    redirige a la pantalla del listado de centros.
    """
    params = request.form
    mensaje = Center.delete(params)
    if os.path.exists('app/static/uploads/centro' + params['id'] +'.pdf'):
        os.remove('app/static/uploads/centro' + params['id'] +'.pdf')
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("centers"))


def commit_update():
    """Llama a la función que realiza la actualización de datos de un centro y
    redirige a la pantalla del listado de centros si fue exitoso, en caso
    contrario se mantiene en la pantalla actual e informa el error.
    """
    params = request.form
    center = Center.find_by_id(params['id'])
    if request.method == 'POST':
        f = request.files['protocol']
        if f.filename != '':
            if f.filename.rsplit('.', 1)[1].lower() == 'pdf':
                parametros = params.to_dict()
                parametros['protocol'] = secure_filename(f.filename) 
                mensaje = center.update(parametros)
                filename = 'centro' + str(params['id'])
                f.save(os.path.join('app/static/uploads', filename + '.pdf'))
                flash(mensaje[0], mensaje[1])
                return redirect(url_for("centers", num_page=1))    
            else:
                flash('Formato de archivo incorrecto, el protocolo debe ser de tipo pdf', 'danger')
                return redirect(url_for('center_update', id=params['id']))
        else:
            mensaje = center.update(params)
            flash(mensaje[0], mensaje[1])
            return redirect(url_for("centers", num_page=1))
            
@permission_required('center_update')
def update(idcenter):
    """Chequea que exista el centro con el id recibido por parámetro y 
    es redirigido a la pantalla para modificar los datos del centro.
    """
    center = Center.find_by_id(idcenter)
    return render_template("center/update.html", center=center)
    

def listado_municipios():
    url="https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios?per_page=135"
    response = requests.get(url)
    parsed = json.loads(response.text)
    municipios = parsed['data']['Town']
    return municipios

@permission_required('center_show')
def view(idcenter):
    """Retorna una lista con el total de centros 
    """  
    center = Center.find_by_id(idcenter)
    return render_template("center/view.html", center=center)
