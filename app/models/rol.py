
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.schema import Table
from app.db import base
from sqlalchemy.orm import relationship, backref


class Rol (base.Model):
    """La clase Rol está asociada a la clase roles en la base de datos. Tiene el nombre del rol.
    """
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    @classmethod
    def return_roles(cls):
        """El método de clase retorna todos los roles existentes en la base de datos.
        """
        return cls.query.all()

    @classmethod
    def get_name_roles(cls, roles):
        """El método de clase retorna los nombres de los roles recibidos. 

        Args:
            roles (lista): id de roles

        Returns:
            lista: strings de nombres de roles
        """
        roles_user = []
        for rol in roles:
            aRol = base.session.query(Rol).filter(Rol.id == int(rol)).first()
            roles_user.append(aRol)
        return roles_user

    @classmethod
    def get_arrayname_roles(cls, roles):
        """El metodo retorna un arrelgo con los nombres de los roles de los id
            recibidos por parametro
        """
        roles_user = []
        for rol in roles:
            aRol = base.session.query(Rol).filter(Rol.id == int(rol)).first()
            roles_user.append(aRol.name)
        return roles_user

    