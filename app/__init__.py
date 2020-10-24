import pymysql
import os
import inspect

from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from functools import wraps

from app.db import connection
from app.helpers import auth as helper_auth
from app.helpers.auth import authenticated
from app.models.pageSetting import PageSetting
from app.models.rol import Rol
from app.models.user import User
from app.models.usersRoles import UsersRoles
from app.resources import auth
from app.resources.pagesettings import indexPage, updateSettings
from app.resources.user import (
    index as user_index,
    login as auth_login,
    new,
    create,
    commit_delete,
    delete,
    commit_update as userUpdate,
    update_profile
)
from app.resources.user import update as update, search as user_search
from app.resources.user import search as search
from config import config


def create_app(environment="development"):
    """Crea y configura la aplicación Flask, junto a la conexión a la
    base de datos. Además genera las diferentes URLs.
    """

    app = Flask(__name__)

    app.config["SESSION_TYPE"] = "filesystem"
    app.secret_key = "3d6f45a5fc12445dbac2f59c3b6c7cb1"
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    Session(app)

    connection(app)

    def role_required(role_name):
        def decorator(func):
            @wraps(func)
            def authorize(*args, **kwargs):
              if not authenticated(session):
                return render_template("error.html")
              user_roles = UsersRoles.find_user_roles_by_id(int(session["id"]))
              name_roles = Rol.get_arrayname_roles(user_roles)
              if role_name not in name_roles:
                  return render_template("error.html")
              return func(*args, **kwargs)

            return authorize

        return decorator

    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

    # Autenticación
    app.add_url_rule("/login", "auth_login", auth_login)  # Url login
    app.add_url_rule("/logout", "auth_logout", auth.logout)  # Url cerrar sesión
    
    @app.route("/users_create", methods=["POST"])
    @role_required("admin")
    def user_create():
        return create()

    @app.route("/users/new")
    @role_required("admin")
    def user_new():
        return new()

    app.add_url_rule("/users/commit_delete", "commit_delete", commit_delete, methods=["POST"])
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])
    app.add_url_rule("/update/profile", "update_profile", update_profile , methods=[ "GET","POST"])


    @app.route("/users/commit_update", methods=["POST"])
    @role_required("admin")
    def commit_update():
        return userUpdate()

    @app.route("/users/update/<int:id>", methods=["GET", "POST"])
    @role_required("admin")
    def user_update(id):
        datos = update(id)
        return render_template(
            "user/update.html",
            user=datos["user"],
            all_roles=datos["all_roles"],
            user_roles=datos["user_roles"],
        )

    # Page Settings
    @app.route("/pageSettings")
    @role_required("admin")
    def pagesettings_indexPage():
        settings = indexPage()
        return render_template("pageConfig/pagesettings.html", settings=settings)

    @app.route("/updateSettings", methods=["POST"])
    @role_required("admin")
    def pagesettings_update():
        """Actualización de información de la página"""
        settings = updateSettings()
        return render_template("pageConfig/pagesettings.html", settings=settings)

    # Rutas de vista de usuarios
    @app.route("/users/<int:num_page>")
    @role_required("admin")
    def usersPag(num_page):
        """Listado de usuarios más búsqueda y ABM."""
        if not authenticated(session):
            return render_template("error.html")
        params = user_index(num_page)
        return render_template("usuarios.html", users=params[0], pages=params[1])

    @app.route("/users/<int:num_page>", methods=["POST"])
    @role_required("admin")
    def usersSearch(num_page):
        """Listado de usuarios más búsqueda y ABM."""
        if not authenticated(session):
            return render_template("error.html")
        params = user_search()
        return render_template("usuarios.html", users=params[0], pages=params[1])

    @app.route("/users/delete/<int:id>", methods=["GET", "POST"])
    @role_required("admin")
    def user_delete(id):
        """Borrado de usuario por id"""
        user = User.find_by_id(id)
        return render_template("user/delete.html", user=user)

    @app.route ("/user/profile", methods=[ "GET", "POST"])
    def user_profile():
        if not authenticated(session):
            return render_template("error.html")
        user = User.find_by_id(session['id'])
        return render_template("user/profile.html", user=user)

    

    @app.route("/")
    def home():
        """Pagina de inicio"""
        settings = PageSetting.find_settings()
        return render_template("home.html", settings=settings)

    return app
