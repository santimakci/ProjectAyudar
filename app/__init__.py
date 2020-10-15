
from app.models.user import SignupForm
import pymysql
from sqlalchemy import create_engine
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
from app.resources.user import index as user_index, login as auth_login, new, create, user_back,commit_delete,delete,commit_update
from app.resources.user import update as update

from app.models.rol import return_roles

from app.helpers import auth as helper_auth

from app.db import connection
from app.resources import auth
from config import config
""" from resources.index import index as  """
   


def create_app(environment="development"):

    
    app = Flask(__name__) 
    
    app.config["SESSION_TYPE"] = "filesystem"
   # app.config['SQLALCHEMY_ECHO'] = environment == "development"
    app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
    env = os.environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    Session(app)
     
    connection(app) #conexion a la base de datos -renombrar- 

    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

    #Autenticación
    app.add_url_rule("/login", "auth_login", auth_login) # Url login
    app.add_url_rule("/logout", "auth_logout", auth.logout) # Url cerrar sesión
    app.add_url_rule("/user_new", "auth_logout", auth.logout) # Url creación usuario

    roles = return_roles

    app.add_url_rule("/users", "user_index", user_index)

    
    app.add_url_rule("/users", "user_create", create, methods=["POST"]) 
    app.add_url_rule("/users/new", "user_new", new)

    #app.add_url_rule("/users/newPrueba", "user_new", new)


    app.add_url_rule("/users/delete/<int:id>","user_delete",delete)
    app.add_url_rule('/users/commit_delete',"commit_delete",commit_delete, methods=["POST"])

    app.add_url_rule("/users/update/<int:id>","user_update",update)
    app.add_url_rule("/users/commit_update","commit_update",commit_update, methods=["POST"])
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])

    @app.route("/robarTemplates")
    def robarTemplates():
        return render_template("index.html")

    #tutorial (desp borrar)  
    @app.route("/signup/", methods=["GET", "POST"])
    def show_signup_form():
        form = SignupForm()
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            next = request.args.get('next', None)
            if next:
                return redirect(next)
            return redirect(url_for('index'))
        return render_template("signup_form.html", form=form)  

    @app.route("/")
    def home():
       return render_template ("home.html")
    return app 
   









    #Cosas comentadas que en algún momento nos van a servir (?) //@gaston:o borrar, despues.. :D
    """
    @app.route("/users/update",methods=['GET'])
    def user_update():
       # id_prueba = request.args.get('id')
        id_to_update = request.args.get('id')
        import code; code.interact(local=dict(globals(), **locals())) 

        id_update = user_back(id_to_update)

        return render_template("user/update.html",user=id_update)
    
    @app.route("/users/delete")
    def user_delete():
        user_to_delete = user_back(request.args.get('id'))
        return render_template("user/delete.html",user=user_to_delete, methods=["DELETE"])
    
    
    @app.route("/usuarios")
    def usuarios():
        return render_template("usuarios.html") 
        """
    