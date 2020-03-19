from application import app, db
from flask import redirect, render_template, request, url_for
from application.taytteet.models import Tayte

@app.route("/taytteet/", methods=["GET"])
def taytteet_index():
    return render_template("taytteet/lista.html", taytteet = Tayte.query.all())

@app.route("/taytteet/uusi/")
def taytteet_form():
    return render_template("taytteet/uusi.html")

@app.route("/taytteet/<tayte_id>/", methods=["POST"])
def taytteet_set_name(tayte_id):

    t = Tayte.query.get(tayte_id)
    t.name = request.form.get("name")
    db.session().commit()
  
    return redirect(url_for("taytteet_index"))

@app.route("/taytteet/", methods=["POST"])
def taytteet_create():
    t = Tayte(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("taytteet_index"))