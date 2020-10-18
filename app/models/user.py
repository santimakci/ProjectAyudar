from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db import base


class User (base.Model):
    """La clase User se asocia con la tabla users en la base de datos. Tiene email, contraseña, nombre, apellido,
    nombre de usuario, si está activo, la fecha de creación, la última fecha en la que fue modificado, si está borrado 
    y la fecha en la que fue borrado logicamente.
    """
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
    date_deleted = Column(DateTime, default=base.func.now())

    def __init__(self, params):
        """Constructor de la clase User, recibe por parametros en un diccionario email, usuario, nombre, apellido y contraseña.
        """
        self.email = params['email']
        self.username = params['username']
        self.first_name = params['first_name']
        self.last_name = params['last_name']
        self.password = params['password']

    @classmethod
    def find_by_email_and_pass(cls, mail, password):
        """Filtra los usuarios por email, contraseña y si está activo o no y en caso de existir retorna el usuario correspondiente.

        Args:
            mail (String)
            password (String)
        """
        for user in base.session.query(User).filter(User.email == mail).filter(User.password == password).filter(User.deleted == False).filter(User.active == True):
            return user

    @classmethod
    def find_by_username(cls, username):
        """Filtra por nombre de usuario y en caso de coincidir y que no esté borrado, retorna el usuario.

        Args:
            username (String)

        """
        for user in base.session.query(User).filter(User.username == username).filter(User.deleted == False):
            return user

    @classmethod
    def find_by_email(cls, email):
        """Filtra por email y en caso de coincidir y que el usuario no esté borrado, lo retorna.

        Args:
            email (String)
        """
        for user in base.session.query(User).filter(User.email == email).filter(User.deleted == False):
            return user

    @classmethod
    def find_by_active(cls, active):
        """Filtra por usuarios activos.
        """
        for user in base.session.query(User).filter(User.active == active).filter(User.deleted == False):
            return user

    @classmethod
    def find_by_id(cls, id):
        """Filtra por id de usuario.

        Args:
            id (int)
        """
        for user in base.session.query(User).filter(User.id == id):
            return user

    @classmethod
    def create(self, params):
        """Crea un objeto usuario y lo inserta en la base de datos.

        Args:
            params (dict): recibe los valores a guardar en el objeto user. 

        """
        if (self.find_by_email(params['email']) or self.find_by_username(params['username'])):
            return ("Email o username ya utilizado", "danger")
        user = User(params)
        base.session.add(user)
        base.session.commit()
        return ("Se creo el usuario ", "success")

    @classmethod
    def delete(self, params):
        """Realiza un borrado lógico sobre un usuario existente en la base de datos.

        Args:
            params ([dict)
        """
        user = self.find_by_id(params['id'])
        user.deleted = True
        user.date_deleted = base.func.now()
        base.session.commit()
        return (f'se borro el usuario {user.username}', 'success')

    def update(self, params):
        """Actualiza los datos de un usuario determinado.

        Args:
            params (dict)
        """
        self.username = params['username']
        self.first_name = params['first_name']
        self.last_name = params['last_name']
        self.password = params['password']
        self.email = params['email']
        self.active = bool(int(params['active']))
        base.session.commit()
        return ("Usuario actualizado correctamente", "success")
