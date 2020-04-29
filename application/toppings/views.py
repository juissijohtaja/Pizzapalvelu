from application import app, db, login_required
from application.toppings.models import Topping
from application.toppings.forms import ToppingsForm, ToppingsEditForm

from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user

@app.route("/taytteet/", methods=["GET"])
@login_required(role="ADMIN")
def toppings_index():
    return render_template("toppings/list.html", toppings = Topping.query.all())

@app.route("/taytteet/uusi/")
@login_required(role="ADMIN")
def toppings_form():
    return render_template("toppings/new.html", form = ToppingsForm())

@app.route("/taytteet/<topping_id>/", methods=["GET"])
@login_required(role="ADMIN")
def toppings_get_item(topping_id):
    t = Topping.query.get(topping_id)
    return render_template("toppings/topping.html", topping = t, form = ToppingsEditForm())

@app.route("/taytteet/<topping_id>/", methods=["POST"])
@login_required(role="ADMIN")
def toppings_set_item(topping_id):
    form = ToppingsForm(request.form)
    t = Topping.query.get(topping_id)
    toppingName = form.name.data
    t.name = toppingName.lower()

    if not form.validate():
        return render_template("toppings/topping.html", form = form, topping = t, error = "Tarkista lomake.")

    db.session().commit()

    flash('Täytteen tallennus onnistui.')
    return redirect(url_for("toppings_index"))

@app.route("/taytteet/delete/<topping_id>/", methods=["POST"])
@login_required(role="ADMIN")
def toppings_delete_item(topping_id):  

    t = Topping.query.get(topping_id)
    db.session().delete(t)
    db.session().commit()

    flash('Täytteen poistaminen onnistui.')
    return redirect(url_for("toppings_index"))

@app.route("/taytteet/uusi/", methods=["POST"])
@login_required(role="ADMIN")
def toppings_create():
    form = ToppingsForm(request.form)

    if not form.validate():
        return render_template("toppings/new.html", form = form, error = "Tarkista lomake.")

    toppingName = form.name.data
    t = Topping(toppingName.lower())

    db.session().add(t)
    db.session().commit()
    
    flash('Täytteen lisääminen onnistui.')
    return redirect(url_for("toppings_index"))