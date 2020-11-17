from sqlalchemy import Column, Integer, String, Date, ForeignKey, exists
from app.db import base
from datetime import date, datetime
from app.models.center import Center


class Turn(base.Model):
    __tablename__ = "turns"
    id = Column(Integer, primary_key=True)
    center_id = Column(Integer, ForeignKey("centers.id"))
    email_request = Column(String, unique=False, nullable=False)
    day = Column(Date, unique=False, nullable=False)
    num_block = Column(Integer, unique=True, nullable=False)
    time = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=False, nullable=False)

    def __init__(self, params):
        """Constructor de la clase User, recibe por parametros en un diccionario email, usuario, nombre, apellido y contraseña."""
        self.center_id = params["center_id"]
        self.email_request = params["email"]
        self.day = params["day"]
        self.num_block = params["num_block"]
        self.time = self.hour_dict(params["num_block"])
        self.phone = params["phone"]

    @classmethod
    def create(self, params):
        center = Center.find_by_id(params["center_id"])
        if center.status != "Aceptado":
            return (
                "No se puede reservar turno de un centro que no esté aceptado",
                "danger",
            )
        fecha = params["day"]
        if self.validarFecha(self, fecha):
            turn = Turn(params)
            base.session.add(turn)
            base.session.commit()
            return ("Se creó el turno", "success")
        else:
            return ("Los datos no son válidos", "danger")

    @classmethod
    def turn_exists(self, date, num_block, center):
        turn = (
            base.session.query(Turn)
            .filter(Turn.day == date)
            .filter(Turn.num_block == num_block)
            .filter(Turn.center_id == center)
            .first()
        )
        return turn is not None

    @classmethod
    def get_turns_by_center_id(cls, id):
        turns = []
        for turn in base.session.query(Turn).filter(Turn.center_id == id):
            turns.append(turn)
        return turns

    @classmethod
    def get_turn_by_id(cls, id):
        turn = base.session.query(Turn).filter(Turn.id == id).first()
        return turn

    @classmethod
    def delete(self, params):
        turn = self.get_turn_by_id(params["id"])
        base.session.delete(turn)
        base.session.commit()
        return ("Se eliminó el turno", "success")

    def update(self, params):
        center = Center.find_by_id(params["center_id"])
        if center.status != "Aceptado":
            return (
                "No se puede modificar un turno de un centro que no esté aceptado",
                "danger",
            )
        fecha = params["day"]
        if self.validarFecha(fecha):
            self.email_request = params["email"]
            self.day = params["day"]
            self.num_block = params["num_block"]
            self.time = self.hour_dict(
                params["num_block"]
            )  # le paso el nuevo bloque actualizando la nueva hora
            self.phone = params["phone"]
            base.session.commit()
            return ("Se actualizó el turno", "success")
        else:
            return ("Los datos no son válidos", "danger")

    def validarFecha(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
        hoy = datetime.today()
        return fecha_dt >= hoy

    def hour_dict(self, num_block):

        horarios = {
            "1": "9:00",
            "2": "9:30",
            "3": "10:00",
            "4": "10:30",
            "5": "11:00",
            "6": "11:30",
            "7": "12:00",
            "8": "12:30",
            "9": "13:00",
            "10": "13:30",
            "11": "14:00",
            "12": "14:30",
            "13": "15:00",
            "14": "15:30",
        }

        return horarios[num_block]

    @classmethod
    def get_turns_by_fecha_and_center(self, fecha, idcenter):
        turnos = []
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
        totalturns = (
            base.session.query(Turn)
            .filter(Turn.day == fecha_dt.date())
            .filter(Turn.center_id == idcenter)
        )
        for turno in totalturns:
            turn = {
                "center_id": turno.center_id,
                "turno_id": turno.id,
                "hora_turno": str(turno.time),
            }
            turnos.append(turn)
        return turnos
