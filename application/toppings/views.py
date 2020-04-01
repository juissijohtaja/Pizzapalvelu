from application import app, db
from application.toppings.models import Topping
from application.toppings.forms import ToppingsForm

from flask import render_template, request, redirect, url_for
from flask_login import login_required


@app.route("/taytteet/", methods=["GET"])
@login_required
def toppings_index():
    return render_template("toppings/list.html", toppings = Topping.query.all())

@app.route("/taytteet/uusi/")
@login_required
def toppings_form():
    return render_template("toppings/new.html", form = ToppingsForm())

@app.route("/taytteet/<topping_id>/", methods=["GET"])
@login_required
def toppings_get_item(topping_id):
    t = Topping.query.get(topping_id)
    return render_template("toppings/topping.html", topping = t)

@app.route("/taytteet/<topping_id>/", methods=["POST"])
@login_required
def toppings_set_item(topping_id):
    form = ToppingsForm(request.form)
    t = Topping.query.get(topping_id)

    if not form.validate():
        return render_template("toppings/topping.html", form = form, topping = t, error = "Nimi ei kelpaa.")

    t = Topping.query.get(topping_id)
    t.name = request.form.get("name")
    db.session().commit()
  
    return redirect(url_for("toppings_index"))

@app.route("/taytteet/delete/<topping_id>/", methods=["POST"])
@login_required
def toppings_delete_item(topping_id):  

    t = Topping.query.get(topping_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("toppings_index"))

@app.route("/taytteet/uusi/", methods=["POST"])
@login_required
def toppings_create():
    form = ToppingsForm(request.form)

    if not form.validate():
        return render_template("toppings/new.html", form = form, error = "Tarkista lomake.")

    t = Topping(form.name.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("toppings_index"))