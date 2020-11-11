import pymysql
import os
import inspect

from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from functools import wraps

from app.db import connection
from app.db import close
from app.helpers import auth as helper_auth
from app.helpers.permissions import permissions
from app.helpers.auth import authenticated
from app.models.pageSetting import PageSetting
from app.models.rol import Rol
from app.models.user import User
from app.models.center import Center
from app.models.usersRoles import UsersRoles
from app.resources import auth
from app.resources.center import (
    index as center_index , 
    new as center_new , 
    create as center_create,
    update as center_update,
    commit_update as center_commit_update,
    delete as center_delete,
    commit_delete as center_commit_delete,
    search as center_search,
    listado_municipios,
    view as center_view,
    search as center_search
)
from app.resources.api.center import ( centers as CentersApi, center_by_id )
from app.resources.index import home 
from app.resources.pagesettings import indexPage, updateSettings
from app.resources.user import (
    index as user_index,
    login as auth_login,
    new,
    create,
    commit_delete,
    delete,
    commit_update,
    update_profile,
    profile,
    delete,
    update,
    search as user_search
)
from config import config



def create_app(environment="development"):
    """Crea y configura la aplicación Flask, junto a la conexión a la
    base de datos. Además genera las diferentes URLs.
    """

    app = Flask(__name__)

    app.config["SESSION_TYPE"] = "filesystem"
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    Session(app)

    connection(app)

    @app.after_request
    def after_request_func(response):
        close(app)
        return response

    
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(settings=PageSetting.find_settings)
    app.jinja_env.globals.update(municipios=listado_municipios())
    app.jinja_env.globals.update(user_permisos=permissions)

    

    # Home de la página
    app.add_url_rule("/", "home", home)

    # Autenticación
    app.add_url_rule("/login", "auth_login", auth_login)  # Url login
    app.add_url_rule("/logout", "auth_logout", auth.logout)  # Url cerrar sesión
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

    # User CRUD
    app.add_url_rule("/users/commit_delete", "commit_delete", commit_delete, methods=["POST"])
    app.add_url_rule("/users/commit_update", "commit_update", commit_update, methods=["POST"])
    app.add_url_rule("/users_create", "user_create", create, methods=["POST"])
    app.add_url_rule("/users/new", "user_new", new)
    app.add_url_rule("/users/update/<int:id>", "user_update", update, methods=['GET', 'POST'])
    app.add_url_rule("/users/delete/<int:id>", "user_delete", delete, methods=['GET', 'POST'])

    #Center CRUD
    app.add_url_rule("/centers_create", "center_create", center_create, methods=["POST"])
    app.add_url_rule("/centers/new","center_new",center_new)
    app.add_url_rule("/centers/update/<int:id>", "center_update", center_update, methods=['GET', 'POST'])
    app.add_url_rule("/centers/view/<int:id>", "center_view", center_view, methods=['GET', 'POST'])
    app.add_url_rule("/centers","centers", center_index, methods=['GET', 'POST'])
    app.add_url_rule("/centersresults", "centersSearch", center_search, methods=['GET', 'POST'])

    #consultar el famoso gran center_commit_update (mala convención de nombres?)
    app.add_url_rule("/centers/commit_update", "center_commit_update", center_commit_update, methods=["POST"])
    app.add_url_rule("/centers/delete/<int:id>", "center_delete", center_delete, methods=['GET', 'POST'])
    app.add_url_rule("/centers/commit_delete", "center_commit_delete", center_commit_delete, methods=["POST"])

    # User Profile
    app.add_url_rule("/user/profile", "user_profile", profile, methods=[ "GET", "POST"]) 
    app.add_url_rule("/update/profile", "update_profile", update_profile , methods=[ "GET","POST"])

    # Page setting
    app.add_url_rule("/pageSettings", "pagesettings_indexPage", indexPage)
    app.add_url_rule("/updateSettings", "pagesettings_update", updateSettings, methods=["POST"])

    # Listado de Usuarios / Busqueda de usuarios
    app.add_url_rule("/users", "usersPag", user_index, methods=['GET', 'POST'])
    app.add_url_rule("/usersresults", "usersSearch", user_search, methods=['GET', 'POST'])

    #Listado de URLS de la API de centros
    app.add_url_rule('/centros', "centrosApi", CentersApi, methods=['GET', 'POST'])
    app.add_url_rule('/centros/<int:id>', "centros_id", center_by_id, methods=['GET'])

    
    
    return app
