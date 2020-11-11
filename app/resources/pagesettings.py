from flask import redirect, render_template, request, url_for, session, abort, flash
from app.helpers.auth import authenticated
from datetime import datetime
from app.models.pageSetting import *
from app.helpers.permissions import *


@permission_required('page_settings')
def indexPage():
    """Retorna la página de configuración de la aplicación web.
    """ 
    settings = PageSetting.find_settings()
    return render_template("pageConfig/pagesettings.html", settings=settings)


def updateSettings():
    """Actualiza los valores de configuración de la aplicación web.
    """
    params = request.form
    mensaje = PageSetting.update(params)
    settings = PageSetting.find_settings()
    flash(mensaje)
    return render_template("pageConfig/pagesettings.html", settings=settings)
