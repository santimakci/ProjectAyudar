from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Longblob, Decimal
from app.db import base

class Center (base.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    address = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    open_time = Column(Time, unique=False, nullable=False)
    close_time = Column(Time, unique=False, nullable=False)
    center_type = Column(String, unique=False, nullable=False)
    municipality = Column(String, unique=False, nullable=False)
    web = Column(String, unique=False, nullable=True)
    published = Column(Boolean, default=False)
    protocol = Column(Longblob, nullable=True)
    coordinates = Column(Decimal, nullable=False)
    status = Column(String, default="Pendiente")


    @classmethod
    def create(self, params):
        """Crea un objeto centro y lo inserta en la base de datos.

        Args:
            params (dict): recibe los valores a guardar en el objeto centro. 

        """
        center = Center(params)
        base.session.add(center)
        base.session.commit()
        return ("Se creó el centro ", "success")