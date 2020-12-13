from sqlalchemy import Column, Integer, String, Date, ForeignKey, exists
from app.db import base
from datetime import date, datetime
from app.models.center import Center


class Turn(base.Model):
    """La clase Turn representa a la tabla turns en la base de datos.
    Tiene el id del turno, el id del centro al que pertenece, nombre,
    apellido, email y telefono del solicitante y fecha y hora del turno.
    """

    __tablename__ = "turns"
    id = Column(Integer, primary_key=True)
    center_id = Column(Integer, ForeignKey("centers.id"))
    email_request = Column(String, unique=False, nullable=False)
    name = Column(String, unique=False, nullable=False)
    lastname = Column(String, unique=False, nullable=False)
    phone = Column(String, unique=False, nullable=False)
    day = Column(Date, unique=False, nullable=False)
    num_block = Column(Integer, unique=True, nullable=False)
    time = Column(String, unique=True, nullable=False)

    def __init__(self, params):
        """Constructor de la clase Turn, recibe por parametros en un diccionario email, id de, centro, día, horario, nombre, apellido y teléfono del solicitante."""
        self.center_id = params["center_id"]
        self.email_request = params["email"]
        self.day = params["day"]
        self.num_block = params["num_block"]
        self.time = self.hour_dict(params["num_block"])
        self.phone = params["phone"]
        self.name = params["name"]
        self.lastname = params["lastname"]

    @classmethod
    def create(self, params):
        """Crea el turno, o en caso de error indica el problema"""
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
            return (
                "No se puede crear un turno en una fecha anterior al día de hoy",
                "danger",
            )

    @classmethod
    def turn_exists(self, date, num_block, center):
        """Chequea la existencia de un turno para un centro en una fecha determinada"""
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
        """Retorna los turnos para un centro determinado"""
        turns = []
        for turn in base.session.query(Turn).filter(Turn.center_id == id):
            turns.append(turn)
        return turns

    @classmethod
    def get_turn_by_id(cls, id):
        """Retorna la información de un turno determinado"""
        turn = base.session.query(Turn).filter(Turn.id == id).first()
        return turn

    @classmethod
    def delete(self, params):
        """Elimina un turno determinado"""
        turn = self.get_turn_by_id(params["id"])
        base.session.delete(turn)
        base.session.commit()
        return ("Se eliminó el turno con éxito!", "success")

    def update(self, params):
        """Actualiza la información de un turno"""
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

    @classmethod
    def turns_available(self, date, center):
        fecha_dt = datetime.strptime(date, "%Y-%m-%d")
        turns_id = []
        for turn in (
            base.session.query(Turn)
            .filter(Turn.center_id == center)
            .filter(Turn.day == fecha_dt.date())
        ):
            turns_id.append(turn.num_block)
        return turns_id

    def validarFecha(self, fecha):
        """Valida la fecha del turno"""
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
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
        totalturns = (
            base.session.query(Turn)
            .filter(Turn.day == fecha_dt.date())
            .filter(Turn.center_id == idcenter)
        )
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
        for turno in totalturns:
            if turno.num_block in horarios:
                del horarios[str(turno.num_block)]
        return horarios

    def search_by_email_and_day(search, day, num_page, quantity, centerid):
        """Realiza la búsqueda por email o dia, o ambos y retorna el resultado paginado"""
        if search != "" and day == "":
            turns = (
                base.session.query(Turn)
                .filter(Turn.email_request.like("%" + search + "%"))
                .filter(Turn.center_id == centerid)
                .paginate(per_page=quantity.elements, page=num_page, error_out=True)
            )
        elif search == "" and day != "":
            # Buscar solo por fecha
            date = datetime.strptime(day, "%Y-%m-%d")
            turns = (
                base.session.query(Turn)
                .filter(Turn.day == date)
                .filter(Turn.center_id == centerid)
                .paginate(per_page=quantity.elements, page=num_page, error_out=True)
            )
        else:
            date = datetime.strptime(day, "%Y-%m-%d")
            turns = (
                base.session.query(Turn)
                .filter(Turn.center_id == centerid)
                .filter(Turn.day == date)
                .filter(Turn.email_request.like("%" + search + "%"))
                .paginate(per_page=quantity.elements, page=num_page, error_out=True)
            )
        return turns
