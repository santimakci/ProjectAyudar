import pymysql
from flask import cli
from flask_sqlalchemy import SQLAlchemy


base = SQLAlchemy()


def connection(current_app):
    """Genera la conexión a la base de datos."""
    db_url = "mysql+pymysql://{username}:{password}@{host}/{database}".format(
        username=current_app.config["DB_USER"],
        password=current_app.config["DB_PASS"],
        host=current_app.config["DB_HOST"],
        database=current_app.config["DB_NAME"],
    )
    current_app.config["SESSION_PERMANENT"] = False

    current_app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    current_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    base.init_app(current_app)

    return base


def close(app):
    base.session.close()
    base.engine.dispose()
