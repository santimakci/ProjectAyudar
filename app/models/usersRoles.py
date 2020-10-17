from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.sql.schema import Table
from app.db import base 


class UsersRoles (base.Model):

    __tablename__ = "usersRoles"
    id = Column(Integer, primary_key=True)
    rol_id = Column(Integer, ForeignKey('roles.id'))
    user_id = Column(Integer, ForeignKey('users.id'))    
    

    def __init__(self,rol_id,user_id):
        self.user_id = user_id
        self.rol_id = rol_id
    

    @classmethod
    def get_data(self,user_id, new_roles):
        self.delete_all_roles(user_id)
        isAdmin = self.isAdmin(user_id)
        self.create_user_rol(user_id,new_roles,isAdmin)


    @classmethod
    def isAdmin(cls,user_id):
        q = base.session.query(UsersRoles).filter(UsersRoles.user_id == user_id).filter(UsersRoles.rol_id == 1)
        return base.session.query(q.exists()).scalar()


    @classmethod
    def find_user_roles_by_id(self,id):
        roles = []        
        for rol in base.session.query(UsersRoles).filter(id == UsersRoles.user_id):
            roles.append(rol.rol_id)
        return roles


    @classmethod
    def get_rol(self,rol_id,user_id):
        return base.session.query(UsersRoles).filter(user_id == UsersRoles.user_id).filter(rol_id == UsersRoles.rol_id).first()


    @classmethod
    def delete_all_roles(self,user_id):
        roles = self.find_user_roles_by_id(user_id)
        for rol in roles:           
            if rol != 1:
                base.session.delete(self.get_rol(rol, user_id))
        base.session.commit()   
    

    @classmethod
    def create_user_rol(cls,user_id,new_roles,isAdmin):
        for rol in new_roles:
            if isAdmin:
                if int(rol) != 1:
                    user_rol = UsersRoles(rol, user_id)
                    base.session.add(user_rol)
            else: 
                user_rol = UsersRoles(rol, user_id)
                base.session.add(user_rol)
        base.session.commit()

   
