from application import app, db
from flask import redirect, render_template, request, url_for
from application.pizzas.models import Pizza
from application.toppings.models import Topping
from itertools import islice

from application.pizzatoppings.models import PizzaTopping

@app.route("/", methods=["GET"])
def index():
    pizzas = Pizza.query.limit(30).all()
    pizzasRecommended = islice(pizzas, 3)
    pizzas.sort(key=lambda x: x.price)
    pwp = Pizza.find_pizzas_with_pineapple()
    pwc = Pizza.find_pizzas_with_chili()
    return render_template("index.html", pizzas = pizzas, pizzasRecommended = pizzasRecommended, pineapplePizzas = pwp, chiliPizzas = pwc)
    