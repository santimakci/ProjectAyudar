from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from flask_session import Session
from app.models.user import User


def login():
    return render_template("auth/login.html")


def authenticate():
    params = request.form

    user = User.find_by_email_and_pass(params["email"], params["password"])

    if not user:
        flash("Usuario o clave incorrecto.",'danger')
        return redirect(url_for("auth_login"))

    session["user"] = user.email

    return redirect(url_for("home"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.", 'info')

    return redirect(url_for("auth_login"))
