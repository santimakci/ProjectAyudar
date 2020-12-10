from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.schema import Table
from app.db import base
from app.models.rolesPermissions import RolesPermissions
from app.models.permiso import Permiso


class UsersRoles(base.Model):
    """La clase UsersRoles se asocia con la tabla usersRoles de la base
    de datos. Hace la relación entre users y roles. Contiene el id del
    usuario y el id del rol.
    """

    __tablename__ = "usersRoles"
    id = Column(Integer, primary_key=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    def __init__(self, rol_id, user_id):
        """Constructor de la clase."""
        self.user_id = user_id
        self.rol_id = rol_id

    @classmethod
    def get_data(self, user_id, new_roles):
        self.delete_all_roles(user_id)
        isAdmin = self.isAdmin(user_id)
        self.create_user_rol(user_id, new_roles, isAdmin)

    @classmethod
    def isAdmin(cls, user_id):
        """Retorna un booleano que indica si el usuario con id= user_id tiene el rol admin o no.
        Args:
            user_id (int)

        Returns:
            boolean
        """
        q = (
            base.session.query(UsersRoles)
            .filter(UsersRoles.user_id == user_id)
            .filter(UsersRoles.rol_id == 1)
        )
        return base.session.query(q.exists()).scalar()

    @classmethod
    def find_user_roles_by_id(self, id):
        """Retorna los roles para un usuario determinado.
        Returns:
            [list]: id de roles
        """
        roles = []
        for rol in base.session.query(UsersRoles).filter(id == UsersRoles.user_id):
            roles.append(rol.rol_id)
        return roles

    @classmethod
    def get_rol(self, rol_id, user_id):
        """Busca la existencia de un rol determinado para un usuario determinado."""
        return (
            base.session.query(UsersRoles)
            .filter(user_id == UsersRoles.user_id)
            .filter(rol_id == UsersRoles.rol_id)
            .first()
        )

    @classmethod
    def delete_all_roles(self, user_id):
        """Borra todos los roles para un usuario particular excepto si el rol es de administrador."""
        roles = self.find_user_roles_by_id(user_id)
        for rol in roles:
            if rol != 1:
                base.session.delete(self.get_rol(rol, user_id))
        base.session.commit()

    @classmethod
    def create_user_rol(cls, user_id, new_roles, isAdmin):
        """Crea objetos de tipo UsersRoles con los datos recibidos por parámetros."""
        for rol in new_roles:
            if isAdmin:
                if int(rol) != 1:
                    user_rol = UsersRoles(rol, user_id)
                    base.session.add(user_rol)
            else:
                user_rol = UsersRoles(rol, user_id)
                base.session.add(user_rol)
        base.session.commit()

    @classmethod
    def return_name_permission_by_iduser(cls, iduser):
        """Retorna el nombre de los permisos para un usuario"""
        permisos = (
            base.session.query(Permiso)
            .select_from(UsersRoles)
            .join(RolesPermissions, UsersRoles.rol_id == RolesPermissions.rol_id)
            .join(Permiso, RolesPermissions.permission_id == Permiso.id)
            .filter(UsersRoles.user_id == iduser)
        )
        name_permisos = []
        for permi in permisos:
            name_permisos.append(permi.name)
        return name_permisos