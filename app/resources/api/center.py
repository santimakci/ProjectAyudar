from flask import jsonify
from app.models.center import Center
from flask import request
import json


def index():
    if request.method == "GET":
        centros = Center.return_API_Data()
        return jsonify(centers=centros)
    else:
        params = json.loads(request.data)
        mensaje = Center.create(params)
        if mensaje[1] == 'success':
            return "Se creo el centro"
        else:
            return "Error"