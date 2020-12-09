from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import base
from app.helpers.auth import authenticated
from app.models.user import User
from app.models.rol import Rol
from app.models.usersRoles import UsersRoles
from app.models.pageSetting import PageSetting
from app.models.turn import Turn
from app.models.center import Center
from datetime import date, datetime
from app.helpers.permissions import *


@permission_required("turn_index")
def index(idcenter):
    num_page = int(request.args.get("num_page", 1))
    quantity = PageSetting.find_settings()
    turns_center = (
        base.session.query(Turn)
        .filter(Turn.center_id == idcenter)
        .paginate(per_page=quantity.elements, page=num_page, error_out=True)
    )
    num_pages = turns_center.iter_pages(
        left_edge=2, left_current=2, right_current=2, right_edge=2
    )
    params = []
    params.append(turns_center)
    params.append(num_pages)
    centro = Center.find_by_id(idcenter)

    return render_template(
        "turn/index.html",
        turns=params[0],
        pages=params[1],
        center=idcenter,
        namecenter=centro.name,
    )

@permission_required("turn_index")
def search(idcenter):
    params = request.form.to_dict()
    num_page = int(request.args.get("num_page", 1))
    quantity = PageSetting.find_settings()

    if bool(params) and params["email"] == "" and params["day"] == "":
        turns = (
            base.session.query(Turn)
            .filter(Turn.center_id == idcenter)
            .paginate(per_page=quantity.elements, page=num_page, error_out=True)
        )
    elif not bool(params):
        params["email"] = request.args.get("search", "")
        params["day"] = request.args.get("day", "")
        turns = search_by_email_and_day(
            params["email"], params["day"], num_page, quantity, idcenter
        )
    else:
        turns = search_by_email_and_day(
            params["email"], params["day"], num_page, quantity, idcenter
        )
    num_pages = turns.iter_pages(
        left_edge=2, left_current=2, right_current=2, right_edge=2
    )
    return render_template(
        "turn/index.html",
        turns=turns,
        center=idcenter,
        pages=num_pages,
        day=params["day"],
        search=params["email"],
    )

@permission_required("turn_index")
def search_by_email_and_day(search, day, num_page, quantity, centerid):
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

@permission_required("turn_new")
def pickDate(idcenter):
    today = date.today()
    return render_template("turn/pickDate.html", center=idcenter, today=today)



@permission_required("turn_new")
def new(idcenter):
    time = get_hour_dict()
    date = request.form['day']
    turns_taked = Turn.turns_available(date,idcenter)
    if turns_taked:
        for turn in turns_taked:
            del time[str(turn)]    
    #import code; code.interact(local=dict(globals(), **locals()))
    return render_template("turn/new.html", center=idcenter, time=time, date=date)

@permission_required("turn_new")
def create(idcenter):
    params = request.form
    if not Turn.turn_exists(params["day"], params["num_block"], params["center_id"]):
        mensaje = Turn.create(params)
        flash(mensaje[0], mensaje[1])
    else:
        flash("No se pudo crear el turno", "danger")
    return redirect(url_for("center_turnosDisp", num_page=1, idcenter=idcenter))


@permission_required("turn_show")
def view(idcenter, idturno):
    turno = Turn.get_turn_by_id(idturno)
    time = get_hour_dict()
    today = date.today()
    timeturn = time.get(str(turno.num_block))
    return render_template(
        "turn/view.html",
        turn=turno,
        time=time,
        idcenter=idcenter,
        today=today,
        timeturn=timeturn,
    )


@permission_required("turn_update")
def update(idcenter, idturno):
    turno = Turn.get_turn_by_id(idturno)
    time = get_hour_dict()
    today = date.today()
    timeturn = time.get(str(turno.num_block))
    return render_template(
        "turn/update.html",
        turn=turno,
        time=time,
        idcenter=idcenter,
        today=today,
        timeturn=timeturn,
    )

@permission_required("turn_update")
def commit_update():
    params = request.form
    idcenter = params["center_id"]
    turn = Turn.get_turn_by_id(params["id"])
    mensaje = turn.update(params)
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("center_turnosDisp", num_page=1, idcenter=idcenter))


@permission_required("turn_destroy")
def delete(idcenter, idturno):
    turno = Turn.get_turn_by_id(idturno)
    timeturn = get_hour_dict().get(str(turno.num_block))
    return render_template("turn/delete.html", turn=turno, timeturn=timeturn)

@permission_required("turn_destroy")
def commit_delete():
    params = request.form
    idcenter = params["center_id"]
    mensaje = Turn.delete(params)
    flash(mensaje[0], mensaje[1])
    return redirect(url_for("center_turnosDisp", num_page=1, idcenter=idcenter))


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
