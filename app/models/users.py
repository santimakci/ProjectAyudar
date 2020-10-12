
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Table, ForeignKey   
from app.db import base 
from sqlalchemy.orm import relationship, backref

usuario_rol = Table('usuario_rol', base.metadata,
    Column('usuarios_id', Integer, ForeignKey('usuarios.id')),
    Column('rol_id', Integer, ForeignKey('rol.id') )
) 

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
    users = relationship('User', secondary=usuario_rol, lazy='subquery',
     backref=backref('usuarios', lazy=True))
    


