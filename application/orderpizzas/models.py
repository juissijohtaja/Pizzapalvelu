from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref
from application.orders.models import Order
from application.pizzas.models import Pizza

class OrderPizza(Base):
    __tablename__ = 'order_pizza'

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    order = relationship(Order, backref=backref("order_pizza", cascade="all, delete-orphan"))
    pizza = relationship(Pizza, backref=backref("order_pizza", cascade="all, delete-orphan"))

    def __init__(self, order_id):
        self.order_id = order_id
