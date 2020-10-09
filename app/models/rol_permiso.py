
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey # Importante: importar ForeignKey para claves foráneas  
from app.db import base 
from app.models.permiso import Permiso # Importamos las clases Permiso y Rol
from app.models.rol import Rol

class Rol_permiso (base.model):

    __tablename__ = "rol_permiso"
    id = Column(Integer, primary_key=True)
    id_permiso = Column(Integer,ForeignKey(Permiso.id), nullable=False)
    id_rol = Column(Integer,ForeignKey(Rol.id), nullable=False)

