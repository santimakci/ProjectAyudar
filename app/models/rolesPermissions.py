from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.schema import Table
from app.db import base


class RolesPermissions (base.Model):
    """La clase RolesPermissions representa a la tabla rolesPermissions en la base de datos. Es la relación entre las tablas roles y permisos.
    Tiene el id de rol y el id de permiso.
    """
    __tablename__ = "rolesPermissions"
    id = Column(Integer, primary_key=True)
    rol_id = Column(Integer, ForeignKey('roles.id'))
    permissions_id = Column(Integer, ForeignKey('permissions.id'))
