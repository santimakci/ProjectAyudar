from datetime import datetime

from flask import redirect, render_template, request, url_for, session, abort, flash

from app.db import base
from app.helpers.auth import authenticated
from app.models.center import Center


# Protected resources
def index():
    """Retorna una lista con el total de centros 
    """
    if not authenticated(session):
        return render_template("errors/error.html")
    centers = base.session.query(Center) 
    params = []
    params.append(centers)
    #import code; code.interact(local=dict(globals(), **locals()))
    return render_template("center/centros.html", centers=params[0])

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

def delete(id):
    """Chequea que exista el centro con el id recibido por parámetro y 
    es redirigido a la pantalla para eliminar a un centro"""
    if not authenticated(session):
        return render_template("errors/error.html")    
    center = Center.find_by_id(id)
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

def update(id):
    """Chequea que exista el centro con el id recibido por parámetro y 
    es redirigido a la pantalla para modificar los datos del centro.
    """
    if not authenticated(session):
        return render_template("errors/error.html")
    center = Center.find_by_id(id)
    return render_template("center/update.html", center=center)
    