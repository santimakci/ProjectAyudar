from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from flask_session import Session
from app.models.pageSetting import PageSetting
from app.models.user import User
from app.models.usersRoles import UsersRoles
from app.models.rol import Rol
from app.helpers.auth import authenticated
import hashlib
from app.helpers.permissions import permissions


def login():
    """Inicio de sesión del usuario"""
    return render_template("auth/login.html")


def authenticate():
    """Define si un usuario está autenticado o no y según eso es a que
    parte de la aplicación web lo redirige y con que mensaje.
    """
    params = request.form
    elpass = hashlib.sha512(params["password"].encode("utf-8")).hexdigest()
    user = User.find_by_email_and_pass(params["email"], elpass)
    settings = PageSetting.find_settings()
    if not user:
        flash("Usuario o clave incorrecto.", "danger")
        return redirect(url_for("auth_login"))
    else:
        user_roles = UsersRoles.find_user_roles_by_id(user.id)
        if not (settings.enabled):
            if 1 not in user_roles:
                flash(
                    "El sitio está en mantenimiento, intente de nuevo más tarde",
                    "danger",
                )
                return redirect(url_for("home"))
    session["user"] = user.username
    session["id"] = user.id
    return redirect(url_for("home"))


def logout():
    """Cierra la sesión del usuario."""
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.", "info")

    return redirect(url_for("home"))
