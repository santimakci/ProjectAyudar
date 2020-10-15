
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.schema import Table
from app.db import base 
from sqlalchemy.orm import relationship, backref
#from app.models.user import user_rol

rol_permission = Table('rolesPermissions', base.metadata,
    Column('permissions_id', Integer, ForeignKey('permissions.id')),
    Column('roles_id', Integer, ForeignKey('roles.id') )
) 


class Rol (base.Model):

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    #users_id = Column(Integer, ForeignKey('users.id'))    
    #users = relationship('User', secondary=user_rol, lazy='subquery',
    # backref=backref('users', lazy=True))


    @classmethod 
    def return_roles(cls):
        return cls.query.all()



"""
Para esta etapa, no será obligatorio desarrollar el CRUD de los roles y los permisos, podrán
administrarse desde la base de datos. Los usuarios, roles y permisos sólo podrán ser
administrados por un usuario con rol de Administrador del sistema.
Considerar que un usuario podrá tener más de un rol, y para cada rol se pueden configurar
varios permisos. Los permisos necesarios asociados a cada rol deberán deducirse del
enunciado, ante la duda pueden consultar a su ayudante.


Módulo de usuarios
Desarrollar el módulo usuarios que deberá contemplar al menos la siguiente
funcionalidad:
.....
Asignar o desasignar roles de un usuario, pueden ser varios. En principio se
proponen los siguientes roles: administrador del sistema y operador del centro de
ayuda.
....

Estas en la pagina , agarras un user y con un boton esos que te dan nombres para elegir, elegis un rol y automaticamente se crea con lo que esta
aca , ese rol. 
Yyyyy , le encajamos la relacion , y ZAS

"""