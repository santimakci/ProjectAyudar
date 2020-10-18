from datetime import datetime

from flask import redirect, render_template, request, url_for, session, abort, flash

from app.db import base
from app.helpers.auth import authenticated
from app.models.user import User
from app.models.rol import Rol
from app.models.usersRoles import UsersRoles
from app.models.pageSetting import PageSetting


# Protected resources
def index(num_page):
    """Retorna una lista con el total de usuarios habilitados paginados
    según lo indicado en la configuración, y el iterador sobre las 
    páginas.
    """
    params = []
    quantity = PageSetting.find_settings()
    users = base.session.query(User).filter(User.deleted == False).paginate(
        per_page=quantity.elements, page=num_page, error_out=True)
    num_pages = users.iter_pages(
        left_edge=2, left_current=2, right_current=2, right_edge=2)
    params.append(users)
    params.append(num_pages)
    return params


def login():
    return render_template("auth/login.html")


def new():
    """Retorna todos los roles existentes
    """
    if not authenticated(session):
        return render_template("error.html")
    roles = Rol.return_roles()
    return render_template("user/new.html", roles=roles)


def search():
    """Realiza la búsqueda sobre usuarios por nombre de usuario o si 
    los mismos están activos o bloqueados y retorna el resultado de 
    forma paginada.
    """
    params = request.form
    parametros = []
    quantity = PageSetting.find_settings()
    if params['username'] == '':
        users = base.session.query(User).filter(User.active == params['active']).filter(
            User.deleted == False).paginate(per_page=quantity.elements, page=1, error_out=True)
    else:
        users = base.session.query(User).filter(User.username.like(params['username'] + "%")).filter(
            User.active == params['active']).filter(User.deleted == False).paginate(per_page=quantity.elements, page=1, error_out=True)
    num_pages = users.iter_pages(
        left_edge=2, left_current=2, right_current=2, right_edge=2)
    parametros.append(users)
    parametros.append(num_pages)
    return parametros


def create():
    """Crea un usuario con los valores recibidos.
    """
    params = request.form
    if request.method == 'POST':
        lista = request.form.getlist('roles[]')
    mensaje = User.create(params)
    if mensaje[1] == 'success':
        new_user = User.find_by_username(params['username'])
        UsersRoles.get_data(new_user.id, lista)
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("usersPag", num_page=1))


def delete(id):
    """Chequea que exista el usuario con el id recibido por parámetro y 
    es redirigido a la pantalla para eliminar a un usuario"""
    if not authenticated(session):
        return render_template("error.html")    
    user = User.find_by_id(id)
    return render_template("user/delete.html", user=user)


def commit_delete():
    """Llama a la función que realiza el borrado lógico de un usuario y
    redirige a la pantalla del listado de usuarios.
    """
    params = request.form
    mensaje = User.delete(params)
    flash(mensaje)
    return redirect(url_for("usersPag", num_page=1))


def commit_update():
    """Llama a la función que realiza la actualización de datos de un usuario y
    redirige a la pantalla del listado de usuarios si fue exitoso, en caso 
    contrario se mantiene en la pantalla actual e informa el error.
    """
    params = request.form
    if request.method == 'POST':
        lista = request.form.getlist('roles[]')
    UsersRoles.get_data(params['id'], lista)
    user = User.find_by_id(params['id'])
    mensaje = user.update(params)
    flash(mensaje[0], mensaje[1])
    if mensaje[1] == 'success':
        return redirect(url_for("usersPag", num_page=1))
    else:
        return redirect(url_for('user_update', id=params['id']))


def user_back(id):
    return User.find_by_id(id)


def update(id):
    """Chequea que exista el usuario con el id recibido por parámetro y 
    es redirigido a la pantalla para modificar los datos de un usuario.
    """
    if not authenticated(session):
        return render_template("error.html")
    all_roles = Rol.return_roles()
    user_roles = UsersRoles.find_user_roles_by_id(id)
    roles_name_user = Rol.get_name_roles(user_roles)
    roles = []
    for item in all_roles:
        if item not in roles_name_user:
            roles.append(item)
    user = User.find_by_id(id)
    return render_template("user/update.html", user=user, all_roles=roles, user_roles=roles_name_user)
