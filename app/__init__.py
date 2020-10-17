import pymysql
from sqlalchemy import create_engine
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
from app.resources.user import index as user_index, login as auth_login, new, create, user_back,commit_delete,delete,commit_update
from app.resources.user import update as update
from app.resources.user import search as search

from app.helpers import auth as helper_auth
from app.db import connection
from app.resources import auth
from config import config
from app.resources.pagesettings import indexPage, updateSettings
from app.models.pageSetting import PageSetting
""" from resources.index import index as  """
   


def create_app(environment="development"):

    
    app = Flask(__name__) 
    
    app.config["SESSION_TYPE"] = "filesystem"
   # app.config['SQLALCHEMY_ECHO'] = environment == "development"
    app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    Session(app)
     
    connection(app) #conexion a la base de datos -renombrar- 

    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

    #Autenticación
    app.add_url_rule("/login", "auth_login", auth_login) # Url login
    app.add_url_rule("/logout", "auth_logout", auth.logout) # Url cerrar sesión
    app.add_url_rule("/user_new", "auth_logout", auth.logout) # Url creación usuario

    app.add_url_rule("/users", "user_index", user_index)

    app.add_url_rule("/users", "user_search", search, methods=["POST"]) 

    app.add_url_rule("/users_create", "user_create", create, methods=["POST"]) 


    app.add_url_rule("/users/new", "user_new", new)

    #app.add_url_rule("/users/newPrueba", "user_new", new)


    app.add_url_rule("/users/delete/<int:id>","user_delete",delete)
    app.add_url_rule('/users/commit_delete',"commit_delete",commit_delete, methods=["POST"])

    #Page config
    app.add_url_rule("/pageSettings", "pagesettings_indexPage", indexPage )
    app.add_url_rule("/updateSettings", "pagesettings_update", updateSettings, methods=["POST"] )



    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

    app.add_url_rule("/users/update/<int:id>","user_update",update)
    app.add_url_rule("/users/commit_update","commit_update",commit_update, methods=["POST"])
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])
   

    @app.route("/")
    def home():
       settings=PageSetting.find_settings()
       return render_template ("home.html", settings=settings)

    return app 
   

