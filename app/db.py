import pymysql
from flask import g #LEER QUE HACE LA G DE FLASK 
from flask import cli
from flask_sqlalchemy import SQLAlchemy

base = SQLAlchemy()

def connection(current_app):
    db_url = "mysql+pymysql://{username}:{password}@{host}/{database}".format(
        username=current_app.config["DB_USER"],
        password=current_app.config["DB_PASS"],
        host=current_app.config["DB_HOST"],
        database=current_app.config["DB_NAME"],
    )
    current_app.config["SESSION_PERMANENT"] = False
    current_app.config["SESSION_TYPE"] = "filesystem"
    current_app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    current_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    base.init_app(current_app)
    """ g.db = SQLAlchemy(current_app) """


    return base

#CERRAR CONEXION A LA BASE CON SQLALCHEMY

""" 
def close(e=None):
    #DB.DISPOSE???? 
    conn = g.pop("db_conn", None)

    if conn is not None:
        conn.close()


def init_app(app):
    app.teardown_appcontext(close) """
