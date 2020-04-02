from application import app, db
from application.pizzas.models import Pizza
from application.pizzas.forms import PizzasForm
from application.toppings.models import Topping


from flask import redirect, render_template, request, url_for
from flask_login import login_required

@app.route("/pizzat/", methods=["GET"])
def pizzas_index():
    return render_template("pizzas/list.html", pizzas = Pizza.query.all())

@app.route("/pizzat/uusi/")
@login_required
def pizzas_form():
    return render_template("pizzas/new.html", form = PizzasForm())

@app.route("/pizzat/<pizza_id>/", methods=["GET"])
@login_required
def pizzas_get_item(pizza_id):
    t = Pizza.query.get(pizza_id)
    return render_template("pizzas/pizza.html", pizza = t)

@app.route("/pizzat/<pizza_id>/", methods=["POST"])
def pizzas_set_item(pizza_id):

    t = Pizza.query.get(pizza_id)
    t.name = request.form.get("name")
    t.price = request.form.get("price")
    db.session().commit()
  
    return redirect(url_for("pizzas_index"))

@app.route("/pizzat/uusi/", methods=["POST"])
@login_required
def pizzas_create():
    form = PizzasForm(request.form)

    if not form.validate():
        return render_template("pizzas/new.html", form = form, error = "Tarkista lomake.")

    p = Pizza(form.name.data)
    p.price = form.price.data

    topping_ids = [1,2,3]
    for id in topping_ids:
        topping=Topping.query.get(id)
        if topping is not None:
            p.toppings.append(topping)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pizzas_index"))
