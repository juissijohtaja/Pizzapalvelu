from application import app, db, login_required
from application.auth.models import User
from application.users.forms import UserEditForm

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

@app.route("/kayttajat/", methods=["GET"])
@login_required(role="ADMIN")
def user_index():
    return render_template("users/list.html", users = User.query.all())

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
    u.name = request.form.get("name")
    u.phone = request.form.get("phone")
    u.address = request.form.get("address")
    u.username = request.form.get("username")
    u.password = request.form.get("password")

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

