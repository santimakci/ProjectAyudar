
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.schema import Table
from app.db import base 
from sqlalchemy.orm import relationship, backref


class Rol (base.Model):

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


    @classmethod 
    def return_roles(cls):
        return cls.query.all()
    

    @classmethod
    def get_name_roles(cls, roles):
        roles_user = []
        for rol in roles:
            aRol = base.session.query(Rol).filter(Rol.id == int(rol)).first()
            roles_user.append(aRol)
        return roles_user