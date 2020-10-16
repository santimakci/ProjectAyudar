from flask import redirect, render_template, request, url_for, session, abort, flash
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

def delete(id):
    user = User.find_by_id(id)
    return render_template("user/delete.html",user = user)

def commit_delete():
    params = request.form
    mensaje = User.delete(params)
    flash(mensaje)
    return redirect(url_for("user_index"))

def commit_update():
    params = request.form
    mensaje = User.update(params)
    flash(mensaje[0], mensaje[1])
    if mensaje[1] == 'success':
        return redirect(url_for("user_index"))
    else:
        return redirect(url_for('user_update',id=params['id']))

def user_back(id): #Con esto me traigo el user con tal id
    return User.find_by_id(id)


def update(id):
    #import code; code.interact(local=dict(globals(), **locals()))
    user = User.find_by_id(id)
    return render_template("user/update.html",user = user)
