from application import db
from application.models import Base


class PizzaTopping(Base):
    pizza_id = db.Column(db.Integer, nullable=False)
    topping_id = db.Column(db.Integer, nullable=False)

    def __init__(self, pizza_id):
        self.pizza_id = pizza_id
