from application import app, db
from flask import redirect, render_template, request, url_for
from application.pizzat.models import Pizza

@app.route("/pizzat/", methods=["GET"])
def pizzat_index():
    return render_template("pizzat/lista.html", pizzat = Pizza.query.all())

@app.route("/pizzat/uusi/")
def pizzat_form():
    return render_template("pizzat/uusi.html")

@app.route("/pizzat/<pizza_id>/", methods=["POST"])
def pizzat_set_name(pizza_id):

    t = Pizza.query.get(pizza_id)
    t.name = request.form.get("name")
    db.session().commit()
  
    return redirect(url_for("pizzat_index"))

@app.route("/pizzat/", methods=["POST"])
def pizzat_create():
    t = Pizza(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pizzat_index"))