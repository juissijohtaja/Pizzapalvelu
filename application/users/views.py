from application import app, db, login_required
from application.auth.models import User
from application.users.forms import UserForm, UserEditForm
from application.orders.models import Order

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from datetime import datetime

@app.route("/kayttajat/", methods=["GET"])
@login_required(role="ADMIN")
def user_index():
    return render_template("users/list.html", users = User.query.all())

@app.route("/kayttajat/uusi/")
@login_required(role="ADMIN")
def user_form():
    return render_template("users/new.html", form = UserForm())

@app.route("/kayttajat/uusi/", methods=["POST"])
@login_required(role="ADMIN")
def user_create():
    form = UserForm(request.form)
    
    if not form.validate():
        return render_template("users/new.html", form = form, error = "Tarkista lomake.")

    newuser = User.query.filter_by(username=form.username.data).first()
    if newuser:
        return render_template("users/new.html", form = form, error = "Käyttäjä on jo olemassa.")
                                
    u = User(form.name.data)
    u.phone = form.phone.data
    u.address = form.address.data
    u.admin = form.admin.data
    u.username = form.username.data
    u.password = form.password.data

    db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("user_index"))

@app.route("/kayttajat/<user_id>/", methods=["GET"])
@login_required(role="ADMIN")
def user_get_item(user_id):
    u = User.query.get(user_id)
    return render_template("users/user.html", user = u, form = UserEditForm())

@app.route("/kayttajat/<user_id>/", methods=["POST"])
@login_required(role="ADMIN")
def user_set_item(user_id):
    form = UserEditForm(request.form)
    u = User.query.get(user_id)
    u.name = form.name.data
    u.phone = form.phone.data
    u.address = form.address.data
    u.admin = form.admin.data
    u.username = form.username.data
    u.password = form.password.data

    if not form.validate():
        return render_template("users/user.html", form = form, user = u, error = "Tarkista lomake.")

    db.session().commit()
  
    return redirect(url_for("user_index"))

@app.route("/kayttajat/poista/<user_id>/", methods=["POST"])
@login_required(role="ADMIN")
def user_delete_item(user_id):  

    u = User.query.get(user_id)
    db.session().delete(u)
    db.session().commit()

    return redirect(url_for("user_index"))

@app.route("/oma-tili/<user_id>/", methods=["GET"])
@login_required(role="USER")
def user_my_account(user_id):

    u = User.query.get(user_id)
    my_orders = Order.query.filter_by(account_id = u.id).all()

    for order in my_orders:
        order.dateTimeOrdered = order.date_created.strftime("%H:%M, %d.%m.%Y")
        order.dateTimeUpdated = order.date_modified.strftime("%H:%M, %d.%m.%Y")
      
    if current_user.get_id() != u.id:
        return redirect(url_for("index"))

    return render_template("users/my-account.html", user = u, orders = my_orders)
