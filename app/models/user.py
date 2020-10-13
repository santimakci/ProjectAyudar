
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Table, ForeignKey, update
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

 #   def __init__(self, email, password, username, first_name, last_name):
 #       self.email = email
 #       self.password = password
 #       self.username = username
 #       self.first_name = first_name
 #       self.last_name = last_name
 #       self.active = True
 #       self.date_created = date.today
 #       self.date_updated = date.today
      

    @classmethod
    def find_by_email_and_pass(cls, mail, password):
        for user in base.session.query(User).filter(User.email==mail).filter(User.password==password):
            return user         
    

    @classmethod 
    def find_by_username(cls,username):
        for user in base.session.query(User).filter(User.username==username):
            return user


    @classmethod
    def find_by_email(cls,email):
        for user in base.session.query(User).filter(User.email==email):
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
        return "Se creo el usuario"
        
    @classmethod
    def update(self, params):
        """if (self.find_by_email(params['email']) or self.find_by_username(params['username'])): #Podríamos hacer una función por fuera no?
           return "Email o username ya utilizado" """
        user_to_update = self.find_by_id(params['id']) #ahora tenemos el usuario
        user_to_update.email = params['email']
        user_to_update.password = params['password']
        user_to_update.first_name = params['first_name']
        user_to_update.last_name = params['last_name']
        base.session.commit()
        return "Usuario actualizado correctamente"


        

   


    
