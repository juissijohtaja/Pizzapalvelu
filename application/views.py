from application import app, db
from flask import redirect, render_template, request, url_for
from application.pizzas.models import Pizza
from application.toppings.models import Topping

from application.pizzatoppings.models import PizzaTopping

@app.route("/", methods=["GET"])
def index():
    pizzas = Pizza.query.all()
    return render_template("index.html", pizzas = pizzas, pineapplePizzas=Pizza.find_pizzas_with_pineapple())
    