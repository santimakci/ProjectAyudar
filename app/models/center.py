from enum import unique
from flask import request
from sqlalchemy import Column, Integer, String, Boolean, Time, Numeric
from app.db import base
import datetime


class Center(base.Model):
    """La clase Center se asocia con la tabla centers en la base de datos. Tiene nombre,
    direccion, telefono hora de apertura y de cierre, tipo de centro, municipalidad, web,
    si fue publicado, protocolo, coordenadas y estado.
    """

    __tablename__ = "centers"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    open_time = Column(Time, unique=False, nullable=False)
    close_time = Column(Time, unique=False, nullable=False)
    center_type = Column(String, unique=False, nullable=False)
    municipality = Column(String, unique=False, nullable=False)
    latitude = Column(String, unique=False, nullable=False)
    longitude = Column(String, unique=False, nullable=False)
    web = Column(String, unique=False, nullable=True)
    email = Column(String, unique=False, nullable=True)
    status = Column(String, unique=False, default="Pendiente")
    protocol = Column(String, unique=False, default="")

    def __init__(self, params):
        """Constructor de la clase Center, recibe por parametros en un diccionario."""
        self.name = params["name"]
        self.address = params["address"]
        self.phone = params["phone"]
        self.open_time = params["open_time"]
        self.close_time = params["close_time"]
        self.center_type = params["center_type"]
        self.municipality = params["municipality"]
        if "status" in params.keys():
            self.status = params["status"]
        self.email = params["email"]
        self.latitude = params["lat"]
        self.longitude = params["lng"]
        self.web = params["web"]
        if "protocol" in params.keys():
            self.protocol = params["protocol"]

    @classmethod
    def return_centers_API_Data(cls):
        """Retorna todos los centros como una lista de diccionarios"""
        centros = []
        for center in base.session.query(Center).filter(Center.status == "Aceptado"):
            Dict = {
                "id": center.id,
                "name": center.name,
                "status": center.status,
                "adress": center.address,
                "phone": center.phone,
                "open_time": center.open_time.strftime("%H:%M"),
                "close_time": center.close_time.strftime("%H:%M"),
                "type": center.center_type,
                "web": center.web,
                "email": center.email,
                "lat": center.latitude,
                "lng": center.longitude,
            }
            centros.append(Dict)
        return centros

    @classmethod
    def return_centers_by_type_API_Data(cls):
        """Retorna para cada tipo de centro su cantidad como un diccionario"""
        tipos = {
            "Sangre": base.session.query(Center).filter(Center.status == "Aceptado").filter(Center.center_type == "Sangre").count(),
            "Plasma": base.session.query(Center).filter(Center.status == "Aceptado").filter(Center.center_type == "Plasma").count(),
            "Ropa": base.session.query(Center).filter(Center.status == "Aceptado").filter(Center.center_type == "Ropa").count(),
            "Comida": base.session.query(Center).filter(Center.status == "Aceptado").filter(Center.center_type == "Comida").count(),
        }
        return tipos

    @classmethod
    def find_by_id(cls, id):
        """Filtra por id de centro.
        Args:
            id (int)
        """
        for center in base.session.query(Center).filter(Center.id == id):
            return center

    @classmethod
    def find_by_name(cls, name):
        """Filtra por nombre y en caso de coincidir, lo retorna.

        Args:
            name (String)
        """
        for center in base.session.query(Center).filter(Center.name == name):
            return center

    @classmethod
    def delete(self, params):
        """Realiza un borrado fisico sobre un centro existente en la base de datos.

        Args:
            params ([dict)
        """
        center = self.find_by_id(params["id"])
        base.session.delete(center)
        base.session.commit()
        return (f"Se borró el centro {center.name}", "success")

    @classmethod
    def create(self, params):
        """Crea un objeto centro y lo inserta en la base de datos.

        Args:
            params (dict): recibe los valores a guardar en el objeto centro.

        """
        center = self.find_by_name(params["name"])
        if center:
            return (("El nombre del centro ya existe", "danger"), center.id)
        center = Center(params)
        base.session.add(center)
        base.session.commit()
        return (("Se creó el centro correctamente ", "success"), center.id)

    def update(self, params):
        """Actualiza los datos de un centro determinado.

        Args:
            params (dict)
        """
        center = self.find_by_name(params["name"])
        if center != None and self != center:
            return ("El nombre del centro ya existe", "danger")
        self.name = params["name"]
        self.address = params["address"]
        self.phone = params["phone"]
        self.open_time = params["open_time"]
        self.close_time = params["close_time"]
        self.center_type = params["center_type"]
        self.municipality = params["municipality"]
        self.status = params["status"]
        self.latitude = params["lat"]
        self.longitude = params["lng"]
        self.web = params["web"]
        self.email = params["email"]
        if "protocol" in params.keys():
            self.protocol = params["protocol"]
        base.session.commit()
        return ("Centro actualizado correctamente", "success")

    def search_by_name_and_status(name, status, num_page, quantity):
        """Realiza la búsqueda por nombre y/o estado y retorna los resultados para la página pedida.
        Args:
            name (string): búsqueda por nombre de centro
            status (string): búsqueda por estado de centro (Aceptado, Pendiente o Rechazado)
            num_page (int): página de la que quiere los resultados
            quantity (int): elementos por página
        """
        if name != "" and status == "":
            centers = (
                base.session.query(Center)
                .filter(Center.name.like("%" + name + "%"))
                .paginate(per_page=quantity.elements, page=num_page, error_out=True)
            )
        elif name == "" and status != "":
            centers = (
                base.session.query(Center)
                .filter(Center.status == status)
                .paginate(per_page=quantity.elements, page=num_page, error_out=True)
            )
        else:
            centers = (
                base.session.query(Center)
                .filter(Center.status == status)
                .filter(Center.name.like("%" + name + "%"))
                .paginate(per_page=quantity.elements, page=num_page, error_out=True)
            )
        return centers
