import sys
from flask import jsonify
from app.models.turn import Turn
from flask import request, render_template
from app.models.pageSetting import PageSetting
import json
from json import JSONDecodeError
from datetime import date, datetime
from sqlalchemy.exc import InternalError


def turns(idcenter):
    try:
        if request.args.get("date"):
            time = get_hour_dict()
            fecha = request.args.get("date")
            turnos = Turn.turns_available(fecha, idcenter)
            if turnos:
                for turn in turnos:
                    del time[str(turn)]   
            return jsonify(time)
        fecha = datetime.today().strftime("%Y-%m-%d")
        turnos = Turn.get_turns_by_fecha_and_center(fecha, idcenter)
        return jsonify(turnos)
    except Exception as e:
        return jsonify(detect_error(sys.exc_info()[0], e))


def reserve_turn(idcenter):
    try:
        if request.method == "POST":
            params = json.loads(request.data)
            params["center_id"] = idcenter
            if not Turn.turn_exists(
                params["day"], params["num_block"], params["center_id"]
            ):
                mensaje = Turn.create(params)
                if mensaje[1] == "success":
                    response = {"status": 200, "body": mensaje[0], "turn": params}
                else:
                    response = {"status": 200, "body": mensaje[0]}
                return jsonify(response)
            else:
                response = {"status": 400, "body": "El turno ya existe"}
                return jsonify(response)
    except Exception as e:
        return jsonify(detect_error(sys.exc_info()[0], e))


def detect_error(e, msg):
    if e is ValueError:
        response = {
            "status": 400,
            "body": "La fecha ingresada debe respetar el formato Y-M-D",
        }
        return response
    elif e is KeyError:
        if str(msg) in ["'email'", "'day'", "'num_block'", "'phone'"]:
            response = {"status": 400, "body": "Falta el atributo %s" % str(msg)}
        else:
            response = {
                "status": 400,
                "body": "El atributo %s es incorrecto" % str(msg),
            }
        return response
    elif e is AttributeError:
        response = {"status": 400, "body": "El Centro solicitado no existe"}
        return response
    elif e is InternalError:
        response = {
            "status": 500,
            "body": "Se produjo un error interno de la base de datos verifique que los campos enviados son válidos",
            "error": str(msg),
        }
    elif e is JSONDecodeError:
        response = {
            "status": 400,
            "body": "El JSON recibido como parámetro no es válido, verigfique es esté bien armado",
        }
        return response

def get_hour_dict():
    horarios = {
        "1": "9:00 a 9:30",
        "2": "9:30 a 10:00",
        "3": "10:00 a 10:30",
        "4": "10:30 a 11:00",
        "5": "11:00 a 11:30",
        "6": "11:30 a 12:00",
        "7": "12:00 a 12:30",
        "8": "12:30 a 13:00",
        "9": "13:00 a 13:30",
        "10": "13:30 a 14:00",
        "11": "14:00 a 14:30",
        "12": "14:30 a 15:00",
        "13": "15:00 a 15:30",
        "14": "15:30 a 16:00",
    }
    return horarios
