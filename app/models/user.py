
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Table, ForeignKey   
from app.db import base 
from sqlalchemy.orm import relationship, backref

user_rol = Table('user_rol', base.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('roles_id', Integer, ForeignKey('roles.id') )
) 

class User (base.Model):
    
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(Integer, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    active = Column(Boolean)
    date_updated = Column(DateTime)
    date_created = Column(DateTime)
    users = relationship('User', secondary=user_rol, lazy='subquery',
     backref=backref('usuarios', lazy=True))
    


