from flask import redirect, render_template, request, url_for, session, abort, flash
from app.helpers.auth import authenticated
from datetime import datetime
from app.models.pageSetting import *


def indexPage():
    """Retorna la página de configuración de la aplicación web.
    """
    if not authenticated(session):
        return render_template("error.html")   
    settings = PageSetting.find_settings()
    return render_template("pageConfig/pagesettings.html", settings=settings)


def updateSettings():
    """Actualiza los valores de configuración de la aplicación web.
    """
    params = request.form
    mensaje = PageSetting.update(params)
    flash(mensaje)
    return redirect(url_for("pagesettings_indexPage"))
