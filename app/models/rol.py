
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from app.db import base 
from sqlalchemy.orm import relationship, backref


rol_permission = Table('rol_permiso', base.metadata,
    Column('permissions_id', Integer, ForeignKey('permissions.id')),
    Column('roles_id', Integer, ForeignKey('roles.id') )
) 


class Rol (base.model):

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))
    roles = relationship('Rol', secondary=rol_permission, lazy='subquery',
        backref=backref('rols', lazy=True))
    
