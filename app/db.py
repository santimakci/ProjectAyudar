import pymysql

from flask import current_app
from flask import g #LEER QUE HACE LA G DE FLASK 
from flask import cli
from flask_sqlalchemy import SQLAlchemy



def connection():
    if "db" not in g:
        db_url = "mysql+pymysql://{username}:{password}@{host}/{database}".format(
            username=current_app.config["DB_USER"],
            password=current_app.config["DB_PASS"],
            host=current_app.config["DB_HOST"],
            database=current_app.config["DB_NAME"],
        )
        current_app.config["SESSION_PERMANENT"] = False
        current_app.config["SESSION_TYPE"] = "filesystem"
        current_app.config["SQLALCHEMY_DATABASE_URI"] = db_url
        g.db = SQLAlchemy(current_app)

    return g.db


""" 
def connection():
    if "db_conn" not in g:
        conf = current_app.config
        g.db_conn = pymysql.connect(
            host=conf["DB_HOST"],
            user=conf["DB_USER"],
            password=conf["DB_PASS"],
            db=conf["DB_NAME"],
            cursorclass=pymysql.cursors.DictCursor,
        )

    return g.db_conn


def close(e=None):
    conn = g.pop("db_conn", None)

    if conn is not None:
        conn.close()


def init_app(app):
    app.teardown_appcontext(close) """
