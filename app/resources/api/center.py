from flask import jsonify
from app.models.center import Center
from flask import request
import json


def centers():
    if request.method == "GET":
        centros = Center.return_centers_API_Data()
        return jsonify(centers=centros)
    else:
        params = json.loads(request.data)
        mensaje = Center.create(params)
        if mensaje[1] == 'success':
            return "Se creo el centro"
        else:
            return "Error"

def center_by_id(id):
    center = Center.find_by_id(id)
    dictCenter = {
                'nombre': center.name,
                'direccion': center.address,
                "telefono": center.phone,
                "hora_apertura": center.open_time.strftime('%H:%M'),
                "hora_cierre": center.close_time.strftime('%H:%M'),
                "tipo": center.center_type,
                "web": center.web,
                "email": center.email
                }
    return jsonify(center=dictCenter)