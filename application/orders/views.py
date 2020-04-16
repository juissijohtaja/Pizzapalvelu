from application import app, db, login_required
from application.pizzas.models import Pizza
from application.toppings.models import Topping
from application.orders.models import Order
from application.orders.forms import OrdersForm, OrdersEditForm


from flask import redirect, render_template, request, url_for
from flask_login import current_user

@app.route("/tilaukset/", methods=["GET"])
@login_required(role="ADMIN")
def orders_index():
    return render_template("orders/list.html", orders = Order.query.all())

@app.route("/tilaukset/uusi/")
@login_required(role="ADMIN")
def orders_form():
    return render_template("orders/new.html", form = OrdersForm(), toppings = Topping.query.all())

@app.route("/tilaukset/<order_id>/", methods=["GET"])
@login_required(role="ADMIN")
def orders_get_item(order_id):
    o = Order.query.get(order_id)
    f = OrdersEditForm()
    
    return render_template("orders/order.html", order = o, form = f)

@app.route("/tilaukset/uusi/", methods=["POST"])
@login_required(role="ADMIN")
def orders_create():

    form = OrdersForm(request.form)
    o = Order(form.delivery.data)  
    o.received = False
    o.delivered = False
    o.account_id = current_user.id

    if not form.validate():
        return render_template("orders/new.html", form = form, error = "Tarkista lomake.")

    pizza=Pizza.query.get(1)
    if pizza is not None:
        o.pizzas.append(pizza)  

    db.session().add(o)
    db.session().commit()
  
    return redirect(url_for("orders_index"))

@app.route("/tilaukset/<order_id>/", methods=["POST"])
@login_required(role="ADMIN")
def orders_set_item(order_id):

    form = OrdersEditForm(request.form)
    o = Order.query.get(order_id)

    o.delivery = form.delivery.data
    o.received = form.received.data
    o.delivered = form.delivered.data

    if not form.validate():
        return render_template("orders/order.html", order = o, form = form, error = "Tarkista lomake.")

    db.session().add(o)
    db.session().commit()
  
    return redirect(url_for("orders_index"))

@app.route("/tilaukset/delete/<order_id>/", methods=["POST"])
@login_required(role="ADMIN")
def orders_delete_item(order_id):  

    o = Order.query.get(order_id)
    db.session().delete(o)
    db.session().commit()

    return redirect(url_for("orders_index"))