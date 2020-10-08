
import pymysql
from sqlalchemy import create_engine
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
""" from .models.users import Usuario """

def create_app(environment="development"):

    app = Flask(__name__) 
    env = os.environ.get("FLASK_ENV", environment)
    Session(app)

    @app.route("/")
    def index():
       return render_template ("index.html")

    """ @app.route("/usuarios")
    def usuarios():
        usuarios = Usuario.query.all()
        return render_template("usuarios.html", contenido=usuarios)"""
    return app 
