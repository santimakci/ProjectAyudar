
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from app.db import base 
from sqlalchemy.orm import relationship, backref


rol_permiso = Table('rol_permiso', base.metadata,
    Column('permiso_id', Integer, ForeignKey('permiso.id')),
    Column('rol_id', Integer, ForeignKey('rol.id') )
) 


class Rol (base.model):

    __tablename__ = "rol"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    roles = relationship('Rol', secondary=rol_permiso, lazy='subquery',
        backref=backref('rols', lazy=True))
    
