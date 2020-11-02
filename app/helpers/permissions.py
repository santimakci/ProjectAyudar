def role_required(role_name):
    def decorator(func):
        @wraps(func)
        
            return func(*args, **kwargs)
        return authorize
    return decorator

def authorize(*args, **kwargs):
    if not authenticated(session):
        return render_template("error.html")
    user_roles = UsersRoles.find_user_roles_by_id(int(session["id"]))
    name_roles = Rol.get_arrayname_roles(user_roles)
    if role_name not in name_roles:
        return render_template("error.html")