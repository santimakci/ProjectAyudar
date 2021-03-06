from datetime import datetime

from flask import redirect, render_template, request, url_for, session, abort, flash

from app.db import base
from app.helpers.auth import authenticated
from app.models.user import User
from app.models.rol import Rol
from app.models.usersRoles import UsersRoles
from app.models.pageSetting import PageSetting
from app.helpers.permissions import permission_required


# Protected resources
@permission_required("user_index")
def index():
    """Retorna una lista de usuarios paginada, que puede o no estar filtrada
    por nombre de usuario, o estado, o ambos."""
    params = request.form.to_dict()
    num_page = int(request.args.get("num_page", 1))
    quantity = PageSetting.find_settings()
    if bool(params) and params["username"] == "":
        users = (
            base.session.query(User)
            .filter(User.active == params["active"])
            .paginate(per_page=quantity.elements, page=1, error_out=True)
        )

    elif not bool(params):
        # buscar con parametros get
        params["username"] = request.args.get("search", "")
        params["active"] = request.args.get("active", "1")
        if params["username"] == "" and params["active"] == "1":
            users = base.session.query(User).paginate(
                per_page=quantity.elements, page=num_page, error_out=True
            )
        else:
            users = (
                base.session.query(User)
                .filter(User.username.like("%" + params["username"] + "%"))
                .filter(User.active == params["active"])
                .paginate(per_page=quantity.elements, page=num_page, error_out=True)
            )
    else:
        users = (
            base.session.query(User)
            .filter(User.username.like("%" + params["username"] + "%"))
            .filter(User.active == params["active"])
            .paginate(per_page=quantity.elements, page=num_page, error_out=True)
        )
    num_pages = users.iter_pages(
        left_edge=2, left_current=2, right_current=2, right_edge=2
    )
    return render_template(
        "user/users.html",
        users=users,
        pages=num_pages,
        active=params["active"],
        search=params["username"],
    )


def login():
    """Retorna la vista de inicio de sesión"""
    return render_template("auth/login.html")


def profile():
    """Retorna la vista con la información del perfil del usuario"""
    user = User.find_by_id(session["id"])
    return render_template("user/profile.html", user=user)


def update_profile():
    """Actualiza la información del perfil de un usuario"""
    params = request.form
    user = User.find_by_id(session["id"])
    mensaje = user.update_profile(params=params)
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("user_profile"))


@permission_required("user_new")
def new():
    """Retorna todos los roles existentes"""
    roles = Rol.return_roles()
    return render_template("user/new.html", roles=roles)


def create():
    """Crea un usuario con los valores recibidos."""
    params = request.form
    if request.method == "POST":
        lista = request.form.getlist("roles[]")
    mensaje = User.create(params)
    if mensaje[1] == "success":
        new_user = User.find_by_username(params["username"])
        UsersRoles.get_data(new_user.id, lista)
    else:
        flash(mensaje[0], mensaje[1])
        return redirect(url_for("user_new"))
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("users"))


@permission_required("user_destroy")
def delete(id):
    """Chequea que exista el usuario con el id recibido por parámetro y
    es redirigido a la pantalla para eliminar a un usuario"""
    user = User.find_by_id(id)
    return render_template("user/delete.html", user=user)


def commit_delete():
    """Llama a la función que realiza el borrado fisico de un usuario y
    redirige a la pantalla del listado de usuarios.
    """
    params = request.form
    user_roles = UsersRoles.find_user_roles_by_id(params["id"])
    name_roles = Rol.get_arrayname_roles(user_roles)
    if "admin" not in name_roles:
        mensaje = User.delete(params)
        flash(mensaje[0], mensaje[1])
    else:
        flash("No se puede eliminar un usuario administrador", "danger")
    return redirect(url_for("users"))


def commit_update():
    """Llama a la función que realiza la actualización de datos de un usuario y
    redirige a la pantalla del listado de usuarios si fue exitoso, en caso
    contrario se mantiene en la pantalla actual e informa el error.
    """
    params = request.form
    if request.method == "POST":
        lista = request.form.getlist("roles[]")
    UsersRoles.get_data(params["id"], lista)
    user = User.find_by_id(params["id"])
    try:
        mensaje = user.update(params)
        flash(mensaje[0], mensaje[1])
        return redirect(url_for("users"))
    except:
        flash("Error al ingresar los datos", "danger")
        return redirect(url_for("user_update", id=params["id"]))


@permission_required("user_update")
def update(id):
    """Chequea que exista el usuario con el id recibido por parámetro y
    es redirigido a la pantalla para modificar los datos de un usuario.
    """
    all_roles = Rol.return_roles()
    user_roles = UsersRoles.find_user_roles_by_id(id)
    roles_name_user = Rol.get_name_roles(user_roles)
    roles = []
    for item in all_roles:
        if item not in roles_name_user:
            roles.append(item)
    user = User.find_by_id(id)
    return render_template(
        "user/update.html", user=user, all_roles=roles, user_roles=roles_name_user
    )


@permission_required("user_detail")
def detail(iduser):
    """Retorna la vista de la información de un usuario"""
    user = User.find_by_id(iduser)
    return render_template("user/read.html", user=user)
