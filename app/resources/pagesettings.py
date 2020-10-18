from flask import redirect, render_template, request, url_for, session, abort, flash
from app.helpers.auth import authenticated
from datetime import datetime
from app.models.pageSetting import *


def indexPage():
    if not authenticated(session):
        return render_template("error.html")

    setttings = PageSetting.find_settings()
    return render_template("pageConfig/pagesettings.html", settings=setttings)

def updateSettings():
    params = request.form
    mensaje = PageSetting.update(params)
    flash(mensaje)
    return redirect(url_for("pagesettings_indexPage"))

