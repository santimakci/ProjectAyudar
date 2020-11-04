from app.models.rolesPermissions import *
from app.models.usersRoles import *
from app.models.permiso import *
from flask import Flask, render_template, request, session
from functools import wraps
from app.helpers.auth import authenticated

def permission_required(idPermiso):
    def decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs): 
            if not authenticated(session):
                return render_template("errors/error.html")
            permisos = permissions()
            if idPermiso not in permisos:
                return render_template("errors/error.html")
            return func(*args, **kwargs)
        return wrap
    return decorator

def permissions():
    if authenticated(session):
        user_roles = UsersRoles.find_user_roles_by_id(int(session["id"]))
        user_permisos = RolesPermissions.get_permissions_by_roles(user_roles)
        name_permisos = Permiso.find_name_permission_by_ids(user_permisos)
        return name_permisos
   
    
    
