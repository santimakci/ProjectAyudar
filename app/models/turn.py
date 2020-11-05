from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db import base
from datetime import date,datetime

class Turn (base.Model):
    __tablename__= "turns"
    id = Column(Integer, primary_key=True)
    center_id = Column(Integer, ForeignKey('centers.id'))
    email_request = Column(String, unique=False, nullable=False)
    day = Column(Date, unique=False, nullable=False)
    num_block = Column(Integer, unique=True, nullable=False)
    time = Column(String, unique=True, nullable=False)

    def __init__(self, params):
        """Constructor de la clase User, recibe por parametros en un diccionario email, usuario, nombre, apellido y contraseña.
        """
        self.center_id = params['center_id']
        self.email_request = params['email']
        self.day = params['day']
        self.num_block = params['num_block']
        self.time = self.hour_dict(params['num_block'])   
    
    @classmethod
    def create(self,params): 
        fecha = params['day']
        if self.validarFecha(self,fecha): 
            turn = Turn(params)        
            base.session.add(turn)
            base.session.commit()        
            return ("Se creo el turno", "success")
        else:   
            return ("Los datos no son válidos", "danger")

    
    @classmethod   
    def get_turns_by_center_id(cls,id):
        turns = []
        for turn in base.session.query(Turn).filter(Turn.center_id == id):
            turns.append(turn)
        return turns

    @classmethod
    def get_turn_by_id(cls,id):
        turn = base.session.query(Turn).filter(Turn.id==id).first()
        return turn

    @classmethod
    def delete(self,params):
        turn = self.get_turn_by_id(params['id'])
        base.session.delete(turn)
        base.session.commit()
        return ("Se eliminó el turno","success")
        
        
    def update(self,params):  
        fecha = params['day']
        if self.validarFecha(fecha):
            self.email_request = params['email']
            self.day = params['day']
            self.num_block = params['num_block']
            self.time = self.hour_dict(params['num_block']) #le paso el nuevo bloque actualizando la nueva hora
            base.session.commit()
            return("Se actualizó el turno", "success")
        else:  
            return ("Los datos no son válidos", "danger")



    def validarFecha(self,fecha):
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
        hoy = datetime.today()
        return fecha_dt >= hoy

    
    def hour_dict(self,num_block):
       
        horarios = {'1':'9:00 a 9:30',
        '2':'9:30 a 10:00',
        '3':'10:00 a 10:30',
        '4':'10:30 a 11:00',
        '5':'11:00 a 11:30',
        '6':'11:30 a 12:00',
        '7':'12:00 a 12:30',
        '8':'12:30 a 13:00',
        '9':'13:00 a 13:30',
        '10':'13:30 a 14:00',
        '11':'14:00 a 14:30',
        '12':'14:30 a 15:00',
        '13':'15:00 a 15:30',
        '14':'15:30 a 16:00'}

        return horarios[num_block]
      
                     