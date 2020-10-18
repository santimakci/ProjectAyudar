from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db import base 



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
    deleted = Column(Boolean(), default=False)
    date_deleted= Column(DateTime, default=base.func.now()) 

    
    def __init__ (self, params):
        self.email = params['email']
        self.username = params['username']
        self.first_name = params['first_name']
        self.last_name = params['last_name']
        self.password = params['password']
        

    @classmethod
    def find_by_email_and_pass(cls, mail, password):
        for user in base.session.query(User).filter(User.email==mail).filter(User.password==password).filter(User.deleted==False).filter(User.active==True):
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
    def find_by_active(cls,active):
        for user in base.session.query(User).filter(User.active == active).filter(User.deleted==False):
            return user


    @classmethod
    def find_by_id(cls,id):
        for user in base.session.query(User).filter(User.id==id):
            return user
 
 
    @classmethod
    def create(self, params):
        if (self.find_by_email(params['email']) or self.find_by_username(params['username'])):
            return ("Email o username ya utilizado", "danger")
        user = User( params )
        base.session.add(user)
        base.session.commit()
        return ("Se creo el usuario ", "success")


    @classmethod
    def delete(self,params):
        user = self.find_by_id(params['id'])
        user.deleted = True
        user.date_deleted = base.func.now()
        base.session.commit()
        return f'se borro el usuario {user.username}'


    def update(self,params):
        self.username = params['username']
        self.first_name = params['first_name']
        self.last_name = params['last_name']
        self.password = params['password']
        self.email = params['email']
        self.active = bool(int(params['active']))
        base.session.commit()
        return ("Usuario actualizado correctamente", "success")  
       