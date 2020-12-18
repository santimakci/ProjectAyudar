import sys
from flask import jsonify
from app.models.center import Center
from flask import request, render_template
from sqlalchemy.exc import InternalError
from app.models.pageSetting import PageSetting
import json


def centers():
    try:
        if request.method == "GET":
            centros = Center.return_centers_API_Data()
            count = len(centros)
            page = int(request.args.get("page", 1))
            limit = (PageSetting.find_settings()).elements
            if 0 >= page:
                return render_template("errors/error404.html")
            obj = {}
            obj["page"] = page
            obj["limit"] = limit
            obj["count"] = count
            obj["centros"] = centros[(page - 1) * limit : (page * limit)]
            return jsonify(obj)
        else:
            params = json.loads(request.data)
            mensaje = Center.create(params)
            if mensaje[0][1] == "success":
                response = {"status": 201, "body": mensaje[0][0], "center": params}
            else:
                response = {"status": 409, "body": mensaje[0][0]}
            return jsonify(response), response.status
    except Exception as e:
        return jsonify(detect_error(sys.exc_info()[0], e))
        
def centers_by_type():
    centros = Center.return_centers_by_type_API_Data()
    return jsonify(centros)



def detect_error(e, msg):
    if e is ValueError:
        response = {"status": 400, "body": "El atributo page debe ser numérico"}
    elif e is KeyError:
        response = {"status": 400, "body": "Falta el atributo %s" % str(msg)}
    elif e is AttributeError:
        response = {"status": 400, "body": "El Centro solicitado no existe"}
    elif e is InternalError:
        response = {
            "status": 500,
            "body": "Se produjo un error interno de la base de datos verifique que los campos enviados son válidos",
            "error": str(msg),
        }
    else:
        response = {
            "status": 500,
            "body": "Se produjo un error interno de la base de datos verifique que los campos enviados son válidos",
            "error": str(msg),
        }
    return response


def center_by_id(id):
    try:
        center = Center.find_by_id(id)
        dictCenter = {
            "name": center.name,
            "address": center.address,
            "phone": center.phone,
            "open_time": center.open_time.strftime("%H:%M"),
            "close_time": center.close_time.strftime("%H:%M"),
            "cente_type": center.center_type,
            "latitude": center.latitude,
            "longitude": center.longitude,
            "web": center.web,
            "email": center.email,
        }
        return jsonify(dictCenter)
    except Exception as e:
        return jsonify(detect_error(sys.exc_info()[0], e))
