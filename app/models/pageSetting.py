
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime 
from app.db import base 

class PageSetting (base.Model):
    
    __tablename__ = "pageSettings"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    title = Column(String, nullable=False)
    enabled = Column(Boolean, nullable=False)
    elements = Column(Integer, nullable=False)


    @classmethod
    def find_settings(cls):
        return base.session.query(PageSetting).first()


    @classmethod
    def update(self, params):
        page = self.find_settings() 
        page.email = params['email']
        page.title = params['title']
        page.description = params['description']
        if len(params) == 4:
            page.enabled = False
        else:
            page.enabled = True
        page.elements = int(params['cant_elements'])
        base.session.commit()
        return "Pagina actualizada correctamente"

             


