from flask import render_template


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }
    return render_template("errors/error.html", **kwargs), 404


def internal_server_error(e):
    kwargs = {
        "status": "500",
        "error_description": "Se produjo un error en el servidor",
    }
    return kwargs, 500


def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No está autorizado para acceder a la url",
    }
    return render_template("errors/error.html", **kwargs), 401
