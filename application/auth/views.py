from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm



@app.route("/auth/login/", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Käyttäjätunnus tai salasana ei kelpaa.")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/signup/", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signupform.html", form = SignupForm())

    form = SignupForm(request.form)
    # mahdolliset validoinnit

    if not form.validate():
        return render_template("auth/signupform.html", form = form, error = "Täytä kaikki lomakkeen tiedot.")

    newuser = User.query.filter_by(username=form.username.data).first()
    if newuser:
        return render_template("auth/signupform.html", form = form,
                                error = "Käyttäjä on jo olemassa.")
                                
    

    u = User(form.name.data)
    u.phone = form.phone.data
    u.address = form.address.data
    u.username = form.username.data
    u.password = form.password.data
    

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))
