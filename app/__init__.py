
import pymysql
from sqlalchemy import create_engine
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
from app.resources.user import index as user_index
from app.helpers import auth as helper_auth
from app.db import connection
from config import config
""" from resources.index import index as  """
   


def create_app(environment="development"):

    
    app = Flask(__name__) 
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    Session(app)
     
    connection(app) #conexion a la base de datos -renombrar- 

    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

    app.add_url_rule("/usuarios", "user_index", user_index)

    @app.route("/")
    def index():
       return render_template ("index.html")

    """ @app.route("/usuarios")
    def usuarios():
        return render_template("usuarios.html") """
    
    return app 
