from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from app.db import base


class Permiso (base.model):
    """La clase Permiso se asocia con la clase permissions en la base de datos. Contiene el nombre del permiso.
    """
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


@classmethod
def create(self, params):
    """Crea un objeto Permiso y lo inserta en la base de datos.

        Args:
            params (dict): recibe los valores a guardar en el objeto Permiso. 

    """
    permiso = Permiso(params)
    base.session.add(permiso)
    base.session.commit()
    return ("Se creó el permiso", "success")

@classmethod
def find_permission_by_id(self,id):
    """Devuelve un permiso por su id
    Args:
        id(int)
    """
    return base.session.query(Permiso).filter(Permiso.id == id).first()
        
def update_permission_name(self, params)
    self.name = params['name']
    base.session.commit()
    return ("Nombre del permiso actualizado correctamente", "success")

@classmethod
def delete(self, params):
    """Elimina un permiso por su id

    """
    permission = self.find_permission_by_id(params['id'])
    base.session.delete(permission)
    base.session.commit()
    return (f'se borro el permiso {permissions.name}', 'success')




