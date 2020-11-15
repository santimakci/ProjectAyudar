from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

from app.db import base


class PageSetting(base.Model):
    """PageSetting es el modelo de la tabla PageSettings existente en la base de datos.
    Contiene el email de contacto a mostrar en la aplicación web, la descripción del sitio,
    el título del mismo, si está habilitado o no y la cantidad de elementos a mostrar por página.
    """

    __tablename__ = "pageSettings"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    title = Column(String, nullable=False)
    enabled = Column(Boolean, nullable=False)
    elements = Column(Integer, nullable=False)

    @classmethod
    def find_settings(cls):
        """Retorna la configuración del sitio."""
        return base.session.query(PageSetting).first()

    @classmethod
    def update(self, params):
        """Actualiza los valores de configuración en la base de datos, según los recibidos por parámetro.

        Args:
            params (Dict): diccionario con los valores a actualizar.

        Returns:
            String: Retorna un mensaje, indicando que se realizó bien la actualización
        """
        page = self.find_settings()
        page.email = params["email"]
        page.title = params["title"]
        page.description = params["description"]
        if len(params) == 4:
            page.enabled = False
        else:
            page.enabled = True
        page.elements = int(params["cant_elements"])
        base.session.commit()
        return "Pagina actualizada correctamente"
