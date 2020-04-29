from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm
from passlib.hash import pbkdf2_sha256

app.secret_key = 'pizzapalvelu'

@app.route("/auth/login/", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form = form, error = "Tarkista lomake.")
    
    user = User.query.filter_by(username=form.username.data).first()
    verifyPassword = pbkdf2_sha256.verify(form.password.data, user.password)
    if not verifyPassword:
        return render_template("auth/loginform.html", form = form, error = "Käyttäjätunnus tai salasana on väärin.")

    login_user(user)
    flash('Sisäänkirjautuminen onnistui.')
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    flash('Uloskirjautuminen onnistui.')
    return redirect(url_for("index"))

@app.route("/auth/signup/", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signupform.html", form = SignupForm())

    form = SignupForm(request.form)
    if not form.validate():
        return render_template("auth/signupform.html", form = form, error = "Tarkista lomake.")

    newuser = User.query.filter_by(username=form.username.data).first()
    if newuser:
        return render_template("auth/signupform.html", form = form, error = "Käyttäjä on jo olemassa.")
                                
    u = User(form.name.data)
    u.phone = form.phone.data
    u.address = form.address.data
    u.username = form.username.data
    u.password = pbkdf2_sha256.hash(form.password.data)

    db.session().add(u)
    db.session().commit()

    flash('Käyttäjätilin luominen onnistui.')
    return redirect(url_for("index"))
