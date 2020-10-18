from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from flask_session import Session
from app.models.user import User


def login():
    return render_template("auth/login.html")


def authenticate():
    """Define si un usuario está autenticado o no y según eso es a que 
    parte de la aplicación web lo redirige y con que mensaje.
    """
    params = request.form
    user = User.find_by_email_and_pass(params["email"], params["password"])
    if not user:
        flash("Usuario o clave incorrecto.", 'danger')
        return redirect(url_for("auth_login"))
    session["user"] = user.email
    return redirect(url_for("home"))


def logout():
    """Cierra la sesión del usuario.
    """
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.", 'info')

    return redirect(url_for("auth_login"))
