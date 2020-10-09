
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime 
from app.db import base 

class PagConfig (base.Model):
    
    __tablename__ = "pagConfig"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    titulo = Column(String, nullable=False)
    habilitado = Column(Boolean, nullable=False)
    cant_elementos = Column(Integer, nullable=False)

