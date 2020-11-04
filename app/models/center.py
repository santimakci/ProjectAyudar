from sqlalchemy import Column, Integer, String, Boolean, Time, Numeric
from sqlalchemy.dialects.mysql import LONGBLOB
from app.db import base


#agregar los pdf por ahora en el filesystem personal 

class Center (base.Model):
    """La clase Center se asocia con la tabla centers en la base de datos. Tiene nombre, direccion, telefono
    hora de apertura y de cierre, tipo de centro, municipalidad, web,si fue publicado, protocolo, coordenadas y estado.
    """
    __tablename__= "centers"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    address = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    open_time = Column(Time, unique=False, nullable=False)
    close_time = Column(Time, unique=False, nullable=False)
    center_type = Column(String, unique=False, nullable=False)
    municipality = Column(String, unique=False, nullable=False)
    web = Column(String, unique=False, nullable=True)
    email = Column(String, unique=False, nullable=False)
    published = Column(Boolean, default=False)
    latitude = Column(String,unique=False,nullable=False)
    longitude = Column(String,unique=False, nullable=False)
    status = Column(String, default="Pendiente")

#ver lo de protocolo y las coordenadas
    def __init__(self, params):
        """Constructor de la clase Center, recibe por parametros en un diccionario.
        """
        self.name = params['name']
        self.address = params['address']
        self.phone = params['phone']
        self.open_time = params['open_time']
        self.close_time = params['close_time']    
        self.center_type = params['center_type']
        self.municipality = params['municipality']
        self.email = params['email']
        self.latitude = params['lat']
        self.longitude = params['lng']
        self.web = params['web']

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
        center = self.find_by_id(params['id'])
        base.session.delete(center)
        base.session.commit()
        return (f'Se borró el centro {center.name}', 'success')


    @classmethod
    def create(self, params):
        """Crea un objeto centro y lo inserta en la base de datos.

        Args:
            params (dict): recibe los valores a guardar en el objeto centro. 

        """
        center = Center(params)
        base.session.add(center)
        base.session.commit()
        return ("Se creó el centro correctamente ", "success")

    def update(self, params):
        """Actualiza los datos de un centro determinado.

        Args:
            params (dict)
        """
        self.name = params['name']
        self.address = params['address']
        self.phone = params['phone']
        self.open_time = params['open_time']
        self.close_time = params['close_time']    
        self.center_type = params['center_type']
        self.municipality = params['municipality']
        self.latitude = params['lat']
        self.longitude = params['lng']
        self.web = params['web']
        self.email = params['email']
        base.session.commit()
        return ("Centro actualizado correctamente", "success")

