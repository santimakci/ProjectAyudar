
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime   
from app.db import base 

class User (base.Model):
    
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(Integer, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    activo = Column(Boolean)
    date_updated = Column(DateTime)
    date_created = Column(DateTime)


