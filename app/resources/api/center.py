from flask import jsonify
from app.models.center import Center
from flask import request, render_template
from app.models.pageSetting import PageSetting
import json


def centers():
    if request.method == "GET":
        centros = Center.return_centers_API_Data()
        count = len(centros)
        start = int(request.args.get('page'))
        limit = (PageSetting.find_settings()).elements
        if ((count/limit) < start):    
            return render_template("errors/error404.html")
        obj = {}
        obj['page'] = start
        obj['limit'] = limit
        obj['count'] = count
        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(1, start - limit)
            obj['previous'] = 'localhost:5000/centros' + '?page=%d' % (start_copy)
        # make next url
        if start + limit > count:
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = 'localhost:5000/centros' + '?page=%d' % (start_copy)
        # finally extract result according to bounds
        obj['centros'] = centros[(start - 1):(start - 1 + limit)]
        return jsonify(obj)
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