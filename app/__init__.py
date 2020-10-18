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
from app.resources.user import index as user_index, login as auth_login, new, create, user_back, commit_delete, delete, commit_update
from app.resources.user import update as update, search as user_search
from app.resources.user import search as search
from config import config


def create_app(environment="development"):
    """Crea y configura la aplicación Flask, junto a la conexión a la
    base de datos. Además genera las diferentes URLs.
    """

    app = Flask(__name__)

    app.config["SESSION_TYPE"] = "filesystem"
    app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    Session(app)
     
    connection(app)
    
    def role_required(role_name):
      def decorator(func):
        @wraps(func)
        def authorize(*args, **kwargs):
          user_roles = UsersRoles.find_user_roles_by_id(int(session['id']))
          name_roles = Rol.get_arrayname_roles(user_roles)
          if role_name not in name_roles:
              return render_template("error.html")
          return func(*args, **kwargs)
        return authorize
      return decorator 

    app.jinja_env.globals.update(
        is_authenticated=helper_auth.authenticated)

    # Autenticación
    app.add_url_rule("/login", "auth_login", auth_login)  # Url login
    app.add_url_rule("/logout", "auth_logout",
                     auth.logout)  # Url cerrar sesión
    app.add_url_rule("/user_new", "auth_logout",
                     auth.logout)  # Url creación usuario

    @app.route("/users/<int:num_page>")
    @role_required('admin')
    def usersPag(num_page):
      """Listado de usuarios más búsqueda y ABM.
      """
      if not authenticated(session):
        return render_template("error.html")
      params = user_index(num_page)       
      return  render_template("usuarios.html", users=params[0], pages=params[1])

    @app.route("/users/<int:num_page>", methods=["POST"])
    @role_required('admin')
    def usersSearch(num_page):
      """Listado de usuarios más búsqueda y ABM.
      """
      if not authenticated(session):
        return render_template("error.html")
      params = user_search() 
      return  render_template("usuarios.html", users=params[0], pages=params[1])


    app.add_url_rule("/users_create", "user_create", create, methods=["POST"]) 

    app.add_url_rule("/users_create", "user_create",
                     create, methods=["POST"])

    app.add_url_rule("/users/new", "user_new", new)


    @app.route("/users/delete/<int:id>",  methods = ['GET', 'POST'])
    @role_required('admin')
    def user_delete(id):
        user = User.find_by_id(id)
        return render_template("user/delete.html", user=user)

    app.add_url_rule('/users/commit_delete', "commit_delete",
                     commit_delete, methods=["POST"])
    # Page config
    app.add_url_rule("/pageSettings", "pagesettings_indexPage", indexPage)
    app.add_url_rule("/updateSettings", "pagesettings_update",
                     updateSettings, methods=["POST"])

    app.add_url_rule("/autenticacion", "auth_authenticate",
                     auth.authenticate, methods=["POST"])

    app.add_url_rule("/users/update/<int:id>", "user_update",
                     update, methods=['GET', 'POST'])
    app.add_url_rule("/users/commit_update", "commit_update",
                     commit_update, methods=["POST"])
    app.add_url_rule("/autenticacion", "auth_authenticate",
                     auth.authenticate, methods=["POST"])

    @app.route("/")
    def home():
        settings = PageSetting.find_settings()
        return render_template("/auth/login.html", settings=settings)

    return app
