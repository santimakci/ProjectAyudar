from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

db=SQLAlchemy()

class Usuario (db.Model):

    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.Integer, nullable=False)
    last_name = db.Column(db.Integer, nullable=False)
    username = db.Column(db.Integer, nullable=False)
    activo = db.Column(db.Boolean)
    date_updated = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime)


