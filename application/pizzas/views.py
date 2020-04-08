from application import app, db
from application.pizzas.models import Pizza
from application.pizzas.forms import PizzasForm, PizzasEditForm
from application.toppings.models import Topping

from flask import redirect, render_template, request, url_for
from flask_login import login_required

@app.route("/pizzat/", methods=["GET"])
@login_required
def pizzas_index():
    return render_template("pizzas/list.html", pizzas = Pizza.query.all())

@app.route("/pizzat/uusi/")
@login_required
def pizzas_form():
    return render_template("pizzas/new.html", form = PizzasForm(), toppings = Topping.query.all())

@app.route("/pizzat/<pizza_id>/", methods=["GET"])
@login_required
def pizzas_get_item(pizza_id):
    t = Pizza.query.get(pizza_id)
    return render_template("pizzas/pizza.html", pizza = t, form = PizzasEditForm())

@app.route("/pizzat/<pizza_id>/", methods=["POST"])
@login_required
def pizzas_set_item(pizza_id):
    
    form = PizzasEditForm(request.form)
    p = Pizza.query.get(pizza_id)

    p.name = request.form.get("name")
    p.price = request.form.get("price")
    p.toppings = []

    topping_ids = []
    topping1 = form.topping1.data
    topping2 = form.topping2.data
    topping3 = form.topping3.data
    topping4 = form.topping4.data

    if topping1 not in topping_ids:
        topping_ids.append(topping1)
    if topping2 not in topping_ids:
        topping_ids.append(topping2)
    if topping3 not in topping_ids:
        topping_ids.append(topping3)
    if topping4 not in topping_ids:
        topping_ids.append(topping4)

    if not form.validate():
        return render_template("pizzas/pizza.html", pizza = p, form = form, toppings = Topping.query.all(), error = "Tarkista lomake.")

    for id in topping_ids:
        topping=Topping.query.get(id)
        if topping is not None:
            p.toppings.append(topping)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pizzas_index"))

@app.route("/pizzat/uusi/", methods=["POST"])
@login_required
def pizzas_create():

    form = PizzasForm(request.form)
    p = Pizza(form.name.data)
    p.price = form.price.data

    topping1 = form.topping1.data
    topping2 = form.topping2.data
    topping3 = form.topping3.data
    topping4 = form.topping4.data

    topping_ids = []
    if topping1 not in topping_ids:
        topping_ids.append(topping1)
    if topping2 not in topping_ids:
        topping_ids.append(topping2)
    if topping3 not in topping_ids:
        topping_ids.append(topping3)
    if topping4 not in topping_ids:
        topping_ids.append(topping4)

    if not form.validate():
        return render_template("pizzas/new.html", form = form, toppings = Topping.query.all(), error = "Tarkista lomake.")

    for id in topping_ids:
        topping=Topping.query.get(id)
        if topping is not None:
            p.toppings.append(topping)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pizzas_index"))

@app.route("/pizzat/delete/<pizza_id>/", methods=["POST"])
@login_required
def pizzas_delete_item(pizza_id):  

    p = Pizza.query.get(pizza_id)
    db.session().delete(p)
    db.session().commit()

    return redirect(url_for("pizzas_index"))
