from datetime import datetime

from flask import redirect, render_template, request, url_for, session, abort, flash

from app.db import base
from app.helpers.auth import authenticated
from app.models.center import Center
from app.models.pageSetting import PageSetting

# Protected resources
def index():
    """Retorna una lista con el total de centros 
    """
    num_page = int(request.args.get('num_page', 1))

    if not authenticated(session):
        return render_template("errors/error.html")
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
    params = request.form
    quantity = PageSetting.find_settings()
    if params['name'] == '':
            centers = base.session.query(Center).paginate(per_page=quantity.elements, page=1, error_out=True)
    else:
        centers = base.session.query(Center).filter(Center.name.like(params['name'] + "%")).paginate(per_page=quantity.elements, page=1, error_out=True)
    num_pages = centers.iter_pages(left_edge=2, left_current=2, right_current=2, right_edge=2)
    return render_template("center/centros.html", centers=centers, pages=num_pages, search=params['name'])


def new():
    if not authenticated(session):
        return render_template("errors/error.html")

    return render_template("center/new.html")
def create():
    """Crea un Centro con los valores recibidos.
    """
    params = request.form
    mensaje = Center.create(params)
    flash(mensaje)
    return redirect(url_for("centers"))

def delete(idcenter):
    """Chequea que exista el centro con el id recibido por parámetro y 
    es redirigido a la pantalla para eliminar a un centro"""
    if not authenticated(session):
        return render_template("errors/error.html")    
    center = Center.find_by_id(idcenter)
    return render_template("center/delete.html", center=center)

def commit_delete():
    """Llama a la función que realiza el borrado fisico de un centro y
    redirige a la pantalla del listado de centros.
    """
    params = request.form
    mensaje = Center.delete(params)
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("centers"))


def commit_update():
    """Llama a la función que realiza la actualización de datos de un centro y
    redirige a la pantalla del listado de centros si fue exitoso, en caso 
    contrario se mantiene en la pantalla actual e informa el error.
    """
    params = request.form
    center = Center.find_by_id(params['id'])
    try:
        mensaje = center.update(params)
        flash(mensaje[0], mensaje[1])  
        return redirect(url_for("centers", num_page=1))
    except: 
        flash('Error al ingresar los datos', 'danger')
        return redirect(url_for('center_update', id=params['id']))

def update(idcenter):
    """Chequea que exista el centro con el id recibido por parámetro y 
    es redirigido a la pantalla para modificar los datos del centro.
    """
    if not authenticated(session):
        return render_template("errors/error.html")
    center = Center.find_by_id(idcenter)
    return render_template("center/update.html", center=center)
    
def view(idcenter):
    """Retorna una lista con el total de centros 
    """
    if not authenticated(session):
        return render_template("errors/error.html")
    
    center = Center.find_by_id(idcenter)
    return render_template("center/view.html", center=center)