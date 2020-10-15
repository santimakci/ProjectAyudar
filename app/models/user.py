#chequear
from os import abort
#ver que onda
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Table, ForeignKey, update
from app.db import base 
from sqlalchemy.orm import relationship, backref
from datetime import date

user_rol = Table('user_rol', base.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('roles_id', Integer, ForeignKey('roles.id') )
) 

class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

class User (base.Model):
    
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(Integer, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    date_updated = Column(DateTime, default=base.func.now())
    date_created = Column(DateTime, default=base.func.now())
    users = relationship('User', secondary=user_rol, lazy='subquery',
     backref=backref('usuarios', lazy=True))
    deleted = Column(Boolean(), default=False)
    date_deleted= Column(DateTime, default=base.func.now()) #en el caso de que se requiera borrar un usuario, se actualiza la fecha de borrado 


    @classmethod
    def find_by_email_and_pass(cls, mail, password):
        for user in base.session.query(User).filter(User.email==mail).filter(User.password==password).filter(User.deleted==False):
            return user         

    @classmethod 
    def find_by_username(cls,username):
        for user in base.session.query(User).filter(User.username==username).filter(User.deleted==False):
            return user

    @classmethod
    def find_by_email(cls,email):
        for user in base.session.query(User).filter(User.email==email).filter(User.deleted==False):
            return user

    @classmethod
    def find_by_id(cls,id):
        for user in base.session.query(User).filter(User.id==id):
            return user

    @classmethod
    def create(self, params):
        if (self.find_by_email(params['email']) or self.find_by_username(params['username'])):
            return "Email o username ya utilizado"
        user = User( **params )
        base.session.add(user)
        base.session.commit()
        return "Se creo el usuario perro"

    @classmethod
    def delete(self,params):
        user = self.find_by_id(params['id'])
        user.deleted = True
        user.date_deleted = base.func.now()
        a = user.username
        base.session.commit()
        return f'se borro el usuario {a}'

    @classmethod
    def update(self,params):

        new_username = params['username'] 
        new_password = params['password'] 
        new_first_name = params['first_name']
        new_last_name = params['last_name'] 
        new_email = params['email']

        old_user = self.find_by_id(params['id'])

        if (new_username != old_user.username):
            if(self.find_by_username(new_username)):
                return "Email o username ya utilizado"

        if (new_email != old_user.email):
            if(self.find_by_email(new_email)):
                return "Email o username ya utilizado"

        #Si llegaste acá, significa que cambiaste el nombre o el email y que no había otro igual, asique todo piola
        old_user.email = new_email
        old_user.username = new_username
        old_user.password = new_password
        old_user.first_name = new_first_name
        old_user.last_name = new_last_name
        base.session.commit()

        return "Usuario actualizado correctamente"