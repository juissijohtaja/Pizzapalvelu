from application import db
from application.models import Base
from application.auth.models import User

from sqlalchemy.orm import relationship
from sqlalchemy.sql import text

class Order(Base):

    __tablename__ = "orders"

    delivery = db.Column(db.String(144), nullable=False)
    oregano = db.Column(db.Boolean, unique=False, default=False)
    garlic = db.Column(db.Boolean, unique=False, default=False)
    received = db.Column(db.Boolean, unique=False, default=False)
    delivered = db.Column(db.Boolean, unique=False, default=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    account = db.relationship(User, foreign_keys=account_id, backref='orders')
    pizzas = relationship("Pizza", secondary="order_pizza")

    def __init__(self, delivery):
        self.delivery = delivery