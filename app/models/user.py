
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
    active = Column(Boolean)
    date_updated = Column(DateTime)
    date_created = Column(DateTime)
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
    def create(self, params):
        if (self.find_by_email(params['email']) or self.find_by_username(params['username'])):
            return "Email o username ya utilizado"
        

   


    
