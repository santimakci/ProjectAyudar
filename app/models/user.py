#chequear
from os import abort

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Table, ForeignKey
from app.db import base 
from sqlalchemy.orm import relationship, backref
from datetime import date

user_rol = Table('user_rol', base.metadata,
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('roles_id', Integer, ForeignKey('roles.id') )
) 

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
    date_deleted= Column(DateTime, default=None) 


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
    def create(self, params):
        if (self.find_by_email(params['email']) or self.find_by_username(params['username'])):
            return "Email o username ya utilizado"
        user = User( **params )
        base.session.add(user)
        base.session.commit()
        return "Se creo el usuario perro"
    
    @classmethod
       #Acción de eliminar usuario.
       #Dejar disponible desde el listado la realización de esta acción. La acción requerirá confirmación para realizarse o para cancelarla.
       #Determinar estrategia de borrado (lógico o físico).
    def delete(id):
        user = User.query.get_or_404(id)
        if user.deleted:
            abort(404)
        user.deleted = True
        user.date_deleted=base.func.now
        base.session.commit()
        return 'se borro el usuario', 204


