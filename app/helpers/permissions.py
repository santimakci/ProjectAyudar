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
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        name_permisos = UsersRoles.return_name_permission_by_iduser(int(session["id"]))
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return name_permisos
