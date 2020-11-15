from flask import jsonify
from app.models.turn import Turn
from flask import request, render_template
from app.models.pageSetting import PageSetting
import json
from datetime import date, datetime


def turns(idcenter):
    if request.args.get("fecha"):
        fecha = request.args.get("fecha")
        turnos = Turn.get_turns_by_fecha_and_center(fecha, idcenter)
        return jsonify(turnos)
    fecha = datetime.today().strftime("%Y-%m-%d")
    turnos = Turn.get_turns_by_fecha_and_center(fecha, idcenter)
    return jsonify(turnos)


def reserve_turn(idcenter):
    if request.method == "POST":
        params = json.loads(request.data)
        if not Turn.turn_exists(
            params["day"], params["num_block"], params["center_id"]
        ):
            mensaje = Turn.create(params)
            return mensaje[0]
        else:
            return "El turno ya existe"
