#chequear
from app.models.rol import Rol
from os import abort
#ver que onda
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Table, ForeignKey, update
from app.db import base 
from sqlalchemy.orm import relationship, backref
from datetime import date

user_rol = Table('usersRoles', base.metadata,
    Column('usuario_id', Integer, ForeignKey('users.id')),
    Column('rol_id', Integer, ForeignKey('roles.id') )
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
    roles = relationship('Rol', secondary=user_rol, lazy='subquery',
        backref=backref('rols', lazy=True))
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
        return "Se creo el usuario "

    #IMPORTANTE Chequear que si está borrado no se pueda loguear
    @classmethod
    def delete(self,params):
        user = self.find_by_id(params['id'])
        user.deleted = True
        user.date_deleted = base.func.now()
        base.session.commit()
        return f'se borro el usuario {user.username}'

    def update(self,params,new_roles):
        self.username = params['username']
        self.first_name = params['first_name']
        self.last_name = params['last_name']
        self.password = params['password']
        import code; code.interact(local=dict(globals(), **locals()))
        self.roles = list(base.session.query(Rol).filter(Rol.id in new_roles))
        base.session.commit()
        return "Usuario actualizado correctamente"   
       