from app.models.rolesPermissions import *
from app.models.usersRoles import *
from flask import session

""" def roles(func):
    def decorator(func):
        @wraps(func)
            permissions()
            return func(*args, **kwargs)
    return decorator """

def authorize(*args, **kwargs):
    if not authenticated(session):
        return render_template("errors/error.html")
    user_roles = UsersRoles.find_user_roles_by_id(int(session["id"]))
    name_roles = Rol.get_arrayname_roles(user_roles)
    if role_name not in name_roles:
        return render_template("errors/error.html")

def permissions():
    #import code; code.interact(local=dict(globals(), **locals()))
    user_roles = UsersRoles.find_user_roles_by_id(int(session["id"]))
    user_permisos = RolesPermissions.get_permissions_by_roles(user_roles)
    return user_permisos
    
    
