from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db import base
import hashlib
from app.models.usersRoles import UsersRoles


class User(base.Model):
    """La clase User se asocia con la tabla users en la base de datos. Tiene email, contraseña, nombre, apellido,
    nombre de usuario, si está activo, la fecha de creación y la última fecha en la que fue modificado.
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

    def __init__(self, params):
        """Constructor de la clase User, recibe por parametros en un diccionario email, usuario, nombre, apellido y contraseña."""
        self.email = params["email"]
        self.username = params["username"]
        self.first_name = params["first_name"]
        self.last_name = params["last_name"]
        self.password = hashlib.sha512(params["password"].encode("utf-8")).hexdigest()

    @classmethod
    def find_by_email_and_pass(cls, mail, password):
        """Filtra los usuarios por email, contraseña y si está activo o no y en caso de existir retorna el usuario correspondiente.

        Args:
            mail (String)
            password (String)
        """
        for user in (
            base.session.query(User)
            .filter(User.email == mail)
            .filter(User.password == password)
            .filter(User.active == True)
        ):
            return user

    @classmethod
    def find_by_username(cls, username):
        """Filtra por nombre de usuario y en caso de coincidir y que no esté borrado, retorna el usuario.

        Args:
            username (String)

        """
        for user in base.session.query(User).filter(User.username == username):
            return user

    @classmethod
    def find_by_email(cls, email):
        """Filtra por email y en caso de coincidir y que el usuario no esté borrado, lo retorna.

        Args:
            email (String)
        """
        for user in base.session.query(User).filter(User.email == email):
            return user

    @classmethod
    def find_by_active(cls, active):
        """Filtra por usuarios activos."""
        for user in base.session.query(User).filter(User.active == active):
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
        if self.find_by_email(params["email"]) or self.find_by_username(
            params["username"]
        ):
            return ("Email o nombre de usuario ya utilizado", "danger")
        user = User(params)
        base.session.add(user)
        base.session.commit()
        return ("Se creó el usuario ", "success")

    @classmethod
    def delete(self, params):
        """Realiza un borrado fisico sobre un usuario existente en la base de datos.

        Args:
            params ([dict)
        """
        user = self.find_by_id(params["id"])
        base.session.delete(user)
        base.session.commit()
        return (f"Se borró el usuario {user.username}", "success")

    def update(self, params):
        """Actualiza los datos de un usuario determinado.

        Args:
            params (dict)
        """
        user = self.find_by_id(params["id"])
        if UsersRoles.isAdmin(user.id) and bool(int(params["active"])) == 0:
            return ("No se puede bloquear un usuario administrador", "danger")
        self.username = params["username"]
        self.first_name = params["first_name"]
        self.last_name = params["last_name"]
        self.email = params["email"]
        self.active = bool(int(params["active"]))
        base.session.commit()
        return ("Usuario actualizado correctamente", "success")

    def update_profile(self, params):
        """Actualiza los datos del perfil del usuario"""
        if params["password"] == "":
            self.first_name = params["first_name"]
            self.last_name = params["last_name"]
            base.session.commit()
            return (
                f"Se actualizó el nombre y apellido del usuario {user.username}",
                "success",
            )

        if (
            params["Newpassword"] != params["Newpassword2"]
            or params["Newpassword"] == ""
        ):
            return ("Error al ingresar la nueva contraseña", "danger")
        if (
            self.password
            == hashlib.sha512(params["password"].encode("utf-8")).hexdigest()
        ):
            self.password = hashlib.sha512(
                params["Newpassword"].encode("utf-8")
            ).hexdigest()
            self.first_name = params["first_name"]
            self.last_name = params["last_name"]
            base.session.commit()
            return ("Usuario actualizado correctamente", "success")
        return ("Error al ingresar la contraseña", "danger")
