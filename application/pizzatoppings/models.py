from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref
from application.toppings.models import Topping
from application.pizzas.models import Pizza

class PizzaTopping(Base):

    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    topping_id = db.Column(db.Integer, db.ForeignKey('topping.id'), nullable=False)

    pizza = relationship(Pizza, backref=backref("pizzatopping", cascade="all, delete-orphan"))
    topping = relationship(Topping, backref=backref("pizzatopping", cascade="all, delete-orphan"))

    def __init__(self, pizza_id):
        self.pizza_id = pizza_id
