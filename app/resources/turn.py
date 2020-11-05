from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import base
from app.helpers.auth import authenticated
from app.models.user import User
from app.models.rol import Rol
from app.models.usersRoles import UsersRoles
from app.models.pageSetting import PageSetting
from app.models.turn import Turn
from datetime import date


def index(idcenter):
    num_page = int(request.args.get('num_page', 1))
    if not authenticated(session):
        return render_template("errors/error.html")
    quantity = PageSetting.find_settings()
    turns_center = base.session.query(Turn).filter(Turn.center_id == idcenter).paginate(per_page=quantity.elements, page=num_page, error_out=True)
    num_pages = turns_center.iter_pages(left_edge=2, left_current=2, right_current=2, right_edge=2) 
    params = []
    params.append(turns_center)
    params.append(num_pages)
    return render_template("turn/index.html", turns=params[0], pages=params[1], center=idcenter)


def new(idcenter):
    if not authenticated(session):
        return render_template("errors/error.html")
    time = get_hour_dict()
    today = date.today()    
    return render_template("turn/new.html",center=idcenter,time=time,today=today)


def create(idcenter):
    params = request.form
    mensaje = Turn.create(params)
    flash(mensaje[0],mensaje[1])
    return redirect(url_for("center_turnosDisp",num_page=1,idcenter=idcenter))


def view(idcenter,idturno):
    if not authenticated(session):
        return render_template("errors/error.html")
    turno = Turn.get_turn_by_id(idturno)
    time = get_hour_dict()
    today = date.today()
    timeturn = time.get(str(turno.num_block))
    return render_template("turn/view.html",turn=turno, time=time, idcenter=idcenter, today=today, timeturn=timeturn)


def update(idcenter,idturno):
    if not authenticated(session):
        return render_template("errors/error.html")
    turno = Turn.get_turn_by_id(idturno)
    time = get_hour_dict()
    today = date.today()
    timeturn = time.get(str(turno.num_block))
    return render_template("turn/update.html",turn=turno, time=time, idcenter=idcenter, today=today, timeturn=timeturn)


def commit_update():
    params = request.form
    idcenter = params['center_id']
    turn = Turn.get_turn_by_id(params['id'])
    mensaje = turn.update(params)
    flash(mensaje[0], mensaje[1])  
    return redirect(url_for("center_turnosDisp", num_page=1, idcenter=idcenter))
   

def delete(idcenter,idturno):    
    if not authenticated(session):
        return render_template("errors/error.html")
    turno = Turn.get_turn_by_id(idturno)    
    timeturn = get_hour_dict().get(str(turno.num_block))
    return render_template("turn/delete.html",turn=turno,timeturn=timeturn)


def commit_delete():
    params = request.form
    idcenter = params['center_id']
    mensaje = Turn.delete(params)    
    flash(mensaje[0], mensaje[1])  
    return redirect(url_for("center_turnosDisp", num_page=1, idcenter=idcenter))

def get_hour_dict():

    horarios = {
    '1':'9:00 a 9:30',
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
    '14':'15:30 a 16:00'
    }
    return horarios


    