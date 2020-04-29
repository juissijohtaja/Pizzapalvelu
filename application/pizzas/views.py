from application import app, db, login_required
from application.pizzas.models import Pizza
from application.pizzas.forms import PizzasForm, PizzasEditForm
from application.toppings.models import Topping

from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user

@app.route("/pizzat/", methods=["GET"])
@login_required(role="ADMIN")
def pizzas_index():
    return render_template("pizzas/list.html", pizzas = Pizza.query.all())

@app.route("/pizzat/uusi/")
@login_required(role="ADMIN")
def pizzas_form():
    return render_template("pizzas/new.html", form = PizzasForm(), toppings = Topping.query.all())

@app.route("/pizzat/<pizza_id>/", methods=["GET"])
@login_required(role="ADMIN")
def pizzas_get_item(pizza_id):
    p = Pizza.query.get(pizza_id)
    f = PizzasEditForm()
    f.topping1.data = p.toppings[0].id
    if len(p.toppings) > 1:
        f.topping2.data = p.toppings[1].id
    if len(p.toppings) > 2:
        f.topping3.data = p.toppings[2].id
    if len(p.toppings) > 3:
        f.topping4.data = p.toppings[3].id
    return render_template("pizzas/pizza.html", pizza = p, form = f)

@app.route("/pizzat/<pizza_id>/", methods=["POST"])
@login_required(role="ADMIN")
def pizzas_set_item(pizza_id):

    form = PizzasEditForm(request.form)
    p = Pizza.query.get(pizza_id)

    p.name = request.form.get("name")
    p.price = request.form.get("price")
    p.toppings = []

    topping1 = form.topping1.data
    topping2 = form.topping2.data
    topping3 = form.topping3.data
    topping4 = form.topping4.data

    if not form.validate():
        return render_template("pizzas/pizza.html", pizza = p, form = form, toppings = Topping.query.all(), error = "Tarkista lomake.")

    toppingList = []
    toppingList.extend((topping1, topping2, topping3, topping4))
    topping_ids = sorted(set(toppingList))

    for id in topping_ids:
        topping=Topping.query.get(id)
        if topping is not None:
            p.toppings.append(topping)

    db.session().add(p)
    db.session().commit()
    
    flash('Pizzan tallennus onnistui.')
    return redirect(url_for("pizzas_index"))

@app.route("/pizzat/uusi/", methods=["POST"])
@login_required(role="ADMIN")
def pizzas_create():

    form = PizzasForm(request.form)
    p = Pizza(form.name.data)
    p.price = form.price.data

    topping1 = form.topping1.data
    topping2 = form.topping2.data
    topping3 = form.topping3.data
    topping4 = form.topping4.data

    if not form.validate():
        return render_template("pizzas/new.html", form = form, toppings = Topping.query.all(), error = "Tarkista lomake.")

    toppingList = []
    toppingList.extend((topping1, topping2, topping3, topping4))
    topping_ids = sorted(set(toppingList))

    for id in topping_ids:
        topping=Topping.query.get(id)
        if topping is not None:
            p.toppings.append(topping)
    
    db.session().add(p)
    db.session().commit()
    
    flash('Pizzan lisääminen onnistui.')
    return redirect(url_for("pizzas_index"))

@app.route("/pizzat/delete/<pizza_id>/", methods=["POST"])
@login_required(role="ADMIN")
def pizzas_delete_item(pizza_id):  

    p = Pizza.query.get(pizza_id)
    db.session().delete(p)
    db.session().commit()

    flash('Pizzan poistaminen onnistui.')
    return redirect(url_for("pizzas_index"))
