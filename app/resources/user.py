from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.user import User
from app.db import base
from app.helpers.auth import authenticated
from datetime import datetime
from app.models.rol import Rol
from app.models.usersRoles import UsersRoles


# Protected resources
def index():
    """ if not authenticated(session):
        abort(401) """
        
    users = base.session.query(User).filter(User.deleted==False)
    return render_template("usuarios.html", users=users)

def login():
    return render_template("auth/login.html")


def new():
    #if not authenticated(session):
    #    abort(401)
    roles = Rol.return_roles()
    return render_template("user/new.html", roles=roles)


def create():
    #if not authenticated(session):
    #    abort(401)
    params = request.form
    if request.method == 'POST':
        lista = request.form.getlist('roles[]')
    mensaje = User.create(params)
    if mensaje[1] == 'success':
        new_user = User.find_by_username(params['username'])
        UsersRoles.get_data(new_user.id,lista)
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("user_index"))


def delete(id):
    user = User.find_by_id(id)
    return render_template("user/delete.html",user = user)


def commit_delete():
    params = request.form
    mensaje = User.delete(params)
    flash(mensaje)
    return redirect(url_for("user_index"))


def commit_update():
    params = request.form    
    if request.method == 'POST':
        lista = request.form.getlist('roles[]')
    UsersRoles.get_data(params['id'],lista)
    user = User.find_by_id(params['id'])   
    mensaje = user.update(params)   
    flash(mensaje[0], mensaje[1])
    if mensaje[1] == 'success':
        return redirect(url_for("user_index"))
    else:
        return redirect(url_for('user_update',id=params['id']))


def user_back(id):
    return User.find_by_id(id)


def update(id):
    all_roles = Rol.return_roles()
    user_roles = UsersRoles.find_user_roles_by_id(id)
    roles_name_user = Rol.get_name_roles(user_roles)    
    roles = []
    for item in all_roles:
        if item not in roles_name_user:
            roles.append(item)
    user = User.find_by_id(id)
    return render_template("user/update.html",user = user, all_roles = roles, user_roles = roles_name_user)



