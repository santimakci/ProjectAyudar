from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection
from app.models.user import User
from app.db import base
from app.helpers.auth import authenticated
from datetime import datetime


# Protected resources
def index():
    """ if not authenticated(session):
        abort(401) """
        
    users = base.session.query(User).filter(User.deleted==False)
    return render_template("usuarios.html", users=users)

def login():
    return render_template("auth/login.html")


def new():
    #if not authenticated(session):
    #    abort(401)
    return render_template("user/new.html")


def create():
    #if not authenticated(session):
    #    abort(401)
    params = request.form
    mensaje = User.create(params)
    flash(mensaje)
    return redirect(url_for("user_index"))


#testing delete 

#def delete(id):
#    return render_template("user/delete.html/{id}")

def commit_delete():
    params = request.form
    mensaje = User.delete(params)
    flash(mensaje)
    return redirect(url_for("user_index"))

def commit_update():
    params = request.form
    mensaje = User.update(params)
    flash(mensaje)
    return redirect(url_for("user_index"))

#def update(id):
#    return render_template("user/update.html")

def user_back(id): #Con esto me traigo el user con tal id
    return User.find_by_id(id)
