from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey   
from app.db import base 

class Permiso (base.model):

    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    roles_id = Column(Integer, ForeignKey('rol.id'))