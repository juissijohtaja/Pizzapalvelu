from application import app, db
from application.pizzas.models import Pizza
from application.pizzas.forms import PizzasForm, PizzasEditForm
from application.toppings.models import Topping


from flask import redirect, render_template, request, url_for
from flask_login import login_required

@app.route("/pizzat/", methods=["GET"])
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
def pizzas_set_item(pizza_id):

    p = Pizza.query.get(pizza_id)
    form = PizzasEditForm(request.form)

    if not form.validate():
        return render_template("pizzas/pizza.html", pizza = p, form = form, toppings = Topping.query.all(), error = "Tarkista lomake.")

    p.name = request.form.get("name")
    p.price = request.form.get("price")
    p.toppings = []

    topping_ids = []
    topping_ids.append(request.form.get("topping1"))
    topping_ids.append(request.form.get("topping2"))
    topping_ids.append(request.form.get("topping3"))
    topping_ids.append(request.form.get("topping4"))

    for id in topping_ids:
        topping=Topping.query.get(id)
        if topping is not None:
            p.toppings.append(topping)

    #db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pizzas_index"))

@app.route("/pizzat/uusi/", methods=["POST"])
@login_required
def pizzas_create():
    form = PizzasForm(request.form)

    if not form.validate():
        return render_template("pizzas/new.html", form = form, toppings = Topping.query.all(), error = "Tarkista lomake.")

    p = Pizza(form.name.data)
    p.price = form.price.data

    topping_ids = []
    topping_ids.append(form.topping1.data)
    topping_ids.append(form.topping2.data)
    topping_ids.append(form.topping3.data)
    topping_ids.append(form.topping4.data)

    for id in topping_ids:
        topping=Topping.query.get(id)
        if topping is not None:
            p.toppings.append(topping)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pizzas_index"))
