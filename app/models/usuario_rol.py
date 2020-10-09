
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey # Importante: importar ForeignKey para claves foráneas  
from app.db import base 
from app.models.users import User # Importamos las clases Permiso y Rol
from app.models.rol import Rol

class Usuario_rol (base.model):

    __tablename__ = "usuario_rol"
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer,ForeignKey(User.id), nullable=False)
    id_rol = Column(Integer,ForeignKey(Rol.id), nullable=False)
