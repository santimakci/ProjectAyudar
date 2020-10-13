
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime 
from app.db import base 

class PageSetting (base.Model):
    
    __tablename__ = "pageSettings"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    title = Column(String, nullable=False)
    enable = Column(Boolean, nullable=False)
    elements = Column(Integer, nullable=False)

