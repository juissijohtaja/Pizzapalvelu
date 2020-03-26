from application import app, db
from flask import redirect, render_template, request, url_for
from application.pizzas.models import Pizza



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", pizzat = Pizza.query.all())