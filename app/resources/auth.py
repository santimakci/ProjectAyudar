from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from flask_session import Session
from app.models.user import User
from app.models.usersRoles import UsersRoles
from app.models.rol import Rol
from app.helpers.auth import authenticated
import hashlib

def login():
    """Inicio de sesión del usuario
    """
    return render_template("auth/login.html")


def authenticate():
    """Define si un usuario está autenticado o no y según eso es a que 
    parte de la aplicación web lo redirige y con que mensaje.
    """
    params = request.form
    elpass = hashlib.md5(params['password'].encode('utf-8')).hexdigest()
    user = User.find_by_email_and_pass(params["email"], elpass)
    if not user:
        flash("Usuario o clave incorrecto.", 'danger')
        return redirect(url_for("auth_login"))
    session["user"] = user.username
    session['id'] = user.id
    user_roles = UsersRoles.find_user_roles_by_id(user.id)
    session['roles'] = Rol.get_name_roles(user_roles)
    return redirect(url_for("home"))


def logout():
    """Cierra la sesión del usuario.
    """
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.", 'info')

    return redirect(url_for("home"))
