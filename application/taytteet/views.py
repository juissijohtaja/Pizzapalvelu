from application import app, db
from application.taytteet.models import Tayte
from application.taytteet.forms import TayteForm

from flask import render_template, request, redirect, url_for
from flask_login import login_required



@app.route("/taytteet/", methods=["GET"])
def taytteet_index():
    return render_template("taytteet/lista.html", taytteet = Tayte.query.all())

@app.route("/taytteet/uusi/")
@login_required
def taytteet_form():
    return render_template("taytteet/uusi.html", form = TayteForm())

@app.route("/taytteet/<tayte_id>/", methods=["POST"])
@login_required
def taytteet_set_name(tayte_id):

    t = Tayte.query.get(tayte_id)
    t.name = request.form.get("name")
    db.session().commit()
  
    return redirect(url_for("taytteet_index"))

@app.route("/taytteet/", methods=["POST"])
@login_required
def taytteet_create():
    form = TayteForm(request.form)

    if not form.validate():
        return render_template("taytteet/uusi.html", form = form)

    t = Tayte(form.name.data)
    t.done = form.done.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("taytteet_index"))