from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import connection
from app.models.user import User
from app.db import base
from app.helpers.auth import authenticated
from datetime import date



# Protected resources
def index():
    """ if not authenticated(session):
        abort(401) """
    users = User.query.all()
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
    username = params['username']
    last_name = params['last_name']
    first_name = params['first_name']
    passw = params['password']
    email = params['email']
    
    user = User( username=username, last_name=last_name, password=passw, 
                email=email, date_updated=date.today, date_created=date.today, active=True)
    base.session.add(user)
    base.session.commit()

    #flash(mensaje)

    return redirect(url_for("user_index"))
