from flask import redirect, render_template, request, url_for, session, abort, flash
from app.helpers.auth import authenticated
from app.models.pageSetting import *


def home():
    """Retorna al login de la pagina
    """
    settings = PageSetting.find_settings()
    return render_template("home.html", settings=settings)