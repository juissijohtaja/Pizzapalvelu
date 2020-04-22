from application import app, db, login_required
from application.pizzas.models import Pizza
from application.toppings.models import Topping
from application.orders.models import Order
from application.orders.forms import OrdersForm, OrdersEditForm


from flask import redirect, render_template, request, url_for
from flask_login import current_user

# orders admin
@app.route("/tilaukset/", methods=["GET"])
@login_required(role="ADMIN")
def orders_index():
    return render_template("orders/list.html", orders = Order.query.all())

@app.route("/tilaukset/<order_id>/", methods=["GET"])
@login_required(role="ADMIN")
def orders_get_item(order_id):
    o = Order.query.get(order_id)
    f = OrdersEditForm()

    f.delivery.default = o.delivery
    f.oregano.default = o.oregano
    f.garlic.default = o.garlic
    f.process()
    
    return render_template("orders/order.html", order = o, form = f)

@app.route("/tilaukset/<order_id>/", methods=["POST"])
@login_required(role="ADMIN")
def orders_set_item(order_id):

    form = OrdersEditForm(request.form)
    o = Order.query.get(order_id)

    o.delivery = form.delivery.data
    o.oregano = form.oregano.data
    o.garlic = form.garlic.data
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

# order as user
@app.route("/tilaa/<pizza_id>", methods=["GET"])
@login_required(role="USER")
def orders_form(pizza_id):
    p = Pizza.query.get(pizza_id)
    return render_template("orders/new.html", form = OrdersForm(), pizza = p, toppings = Topping.query.all())

@app.route("/tilaa/", methods=["POST"])
@login_required(role="USER")
def orders_create():
    form = OrdersForm(request.form)
    o = Order(form.delivery.data)
    o.oregano = form.oregano.data
    o.garlic = form.garlic.data
    o.account_id = current_user.id
    p = Pizza.query.get(form.pizza_id.data)

    if not form.validate():
        return render_template("orders/new.html", form = form, pizza = p, error = "Tarkista lomake.")    

    if p is not None:
        o.pizzas.append(p)  

    db.session().add(o)
    db.session().commit()
  
    return redirect(url_for("index"))
