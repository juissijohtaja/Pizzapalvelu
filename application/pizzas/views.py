from application import app, db
from flask import redirect, render_template, request, url_for
from application.pizzas.models import Pizza

@app.route("/pizzat/", methods=["GET"])
def pizzas_index():
    return render_template("pizzas/list.html", pizzas = Pizza.query.all())

@app.route("/pizzat/uusi/")
def pizzas_form():
    return render_template("pizzas/new.html")

@app.route("/pizzat/<pizza_id>/", methods=["POST"])
def pizzas_set_item(pizza_id):

    t = Pizza.query.get(pizza_id)
    t.name = request.form.get("name")
    db.session().commit()
  
    return redirect(url_for("pizzas_index"))

@app.route("/pizzat/", methods=["POST"])
def pizzas_create():
    t = Pizza(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pizzas_index"))