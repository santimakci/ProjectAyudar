
import pymysql
from sqlalchemy import create_engine
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
from app.resources.user import index as user_index

from app.db import connection
from config import config
""" from resources.index import index as  """
   

""" db = None """

def create_app(environment="development"):

    
    app = Flask(__name__) 
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    Session(app)
    """ import code; code.interact(local=dict(globals(), **locals())) """
     
    connection(app)

    app.add_url_rule("/usuarios", "user_index", user_index)

    @app.route("/")
    def index():
       return render_template ("index.html")

    """ @app.route("/usuarios")
    def usuarios():
        return render_template("usuarios.html") """
    
    return app 
