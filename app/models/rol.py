
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime   
from app.db import base 

class Rol (base.model):

    __tablename__ = "rol"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)