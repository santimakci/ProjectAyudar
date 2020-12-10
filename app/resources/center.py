import os
import requests
import json
from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from werkzeug import secure_filename
from app.db import base
from app.helpers.auth import authenticated
from app.models.center import Center
from app.models.pageSetting import PageSetting
from app.helpers.permissions import *


@permission_required("center_index")
def index():
    """Retorna el listado de centros paginado, y según el caso filtrado por nombre de
    centro o estado, o ambos."""
    params = request.form.to_dict()
    num_page = int(request.args.get("num_page", 1))
    quantity = PageSetting.find_settings()
    if not bool(params):
        params["name"] = request.args.get("name")
        params["status"] = request.args.get("status")
        if params["name"] == "" and params["status"] == "":
            centers = base.session.query(Center).paginate(
                per_page=quantity.elements, page=num_page, error_out=True
            )
        else:
            centers = Center.search_by_name_and_status(
                params["name"], params["status"], num_page, quantity
            )
    else:
        if params["name"] == "" and params["status"] == "":
            centers = base.session.query(Center).paginate(
                per_page=quantity.elements, page=num_page, error_out=True
            )
        else:
            centers = Center.search_by_name_and_status(
                params["name"], params["status"], num_page, quantity
            )
    num_pages = centers.iter_pages(
        left_edge=2, left_current=2, right_current=2, right_edge=2
    )
    return render_template(
        "center/centers.html",
        centers=centers,
        pages=num_pages,
        name=params["name"],
        status=params["status"],
    )


@permission_required("center_new")
def new():
    """Retorna la vista para crear un centro"""
    return render_template("center/new.html")


def create():
    """Crea un Centro con los valores recibidos."""
    params = request.form
    if request.method == "POST":
        f = request.files["protocol"]
        if f.filename != "":
            nombre, extension = os.path.splitext(f.filename)
            if extension == ".pdf":
                parametros = params.to_dict()
                parametros["protocol"] = secure_filename(f.filename)
                param = Center.create(parametros)
                filename = "centro" + str(param[1])
                f.save(os.path.join("app/static/uploads", filename + ".pdf"))
                mensaje = param[0]
            else:
                mensaje = (
                    "Formato de archivo incorrecto, el protocolo debe ser de tipo pdf",
                    "danger",
                )
        else:
            args = Center.create(params)
            mensaje = args[0]
    flash(mensaje[0], mensaje[1])
    if mensaje[1] == "danger":
        return redirect(url_for("center_new"))
    return redirect(url_for("centers", name="", status=""))


@permission_required("center_destroy")
def delete(idcenter):
    """Chequea que exista el centro con el id recibido por parámetro y
    es redirigido a la pantalla para eliminar a un centro"""
    center = Center.find_by_id(idcenter)
    return render_template("center/delete.html", center=center)


def commit_delete():
    """Llama a la función que realiza el borrado fisico de un centro y
    redirige a la pantalla del listado de centros.
    """
    params = request.form
    mensaje = Center.delete(params)
    if os.path.exists("app/static/uploads/centro" + params["id"] + ".pdf"):
        os.remove("app/static/uploads/centro" + params["id"] + ".pdf")
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("centers", name="", status=""))


def commit_update():
    """Llama a la función que realiza la actualización de datos de un centro y
    redirige a la pantalla del listado de centros si fue exitoso, en caso
    contrario se mantiene en la pantalla actual e informa el error.
    """
    params = request.form
    center = Center.find_by_id(params["id"])
    if request.method == "POST":
        f = request.files["protocol"]
        if f.filename != "":
            if f.filename.rsplit(".", 1)[1].lower() == "pdf":
                parametros = params.to_dict()
                parametros["protocol"] = secure_filename(f.filename)
                mensaje = center.update(parametros)
                filename = "centro" + str(params["id"])
                f.save(os.path.join("app/static/uploads", filename + ".pdf"))
            else:
                mensaje = (
                    "Formato de archivo incorrecto, el protocolo debe ser de tipo pdf",
                    "danger",
                )
        else:
            mensaje = center.update(params)
    flash(mensaje[0], mensaje[1])
    if mensaje[1] == "danger":
        return redirect(url_for("center_update", idcenter=params["id"]))
    return redirect(url_for("centers", name="", status=""))


@permission_required("center_update")
def update(idcenter):
    """Chequea que exista el centro con el id recibido por parámetro y
    es redirigido a la pantalla para modificar los datos del centro.
    """
    center = Center.find_by_id(idcenter)
    return render_template("center/update.html", center=center)


def listado_municipios():
    """Retorna los municipios de una página determinada"""
    url = "https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios"
    response = requests.get(url)
    parsed = json.loads(response.text)
    municipios = parsed["data"]["Town"]
    return municipios


@permission_required("center_show")
def view(idcenter):
    """Retorna la información de un centro"""
    center = Center.find_by_id(idcenter)
    return render_template("center/view.html", center=center)
