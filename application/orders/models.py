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

    pizzas = relationship("Pizza", secondary="order_pizza")

    def __init__(self, delivery):
        self.delivery = delivery

    @staticmethod
    def find_user_spend():
        stmt = text("SELECT O.account_id, COUNT(P.id) as amount, SUM(P.price) as spend, A.name"
                        " FROM orders O"
                        " LEFT JOIN order_pizza OP ON O.id = OP.order_id"
                        " LEFT JOIN pizza P ON P.id = OP.pizza_id"
                        " LEFT JOIN account A ON A.id = O.account_id"
                        " GROUP BY O.account_id, A.name"
                        " ORDER BY spend DESC, amount DESC"
                        " LIMIT 3")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"accountId":row[0], "orderCount":row[1], "orderSum":row[2], "userName":row[3]})

        return response
    
    @staticmethod
    def find_top_pizzas():
        stmt = text("SELECT COUNT(O.id) as amount, P.name"
                        " FROM orders O"
                        " LEFT JOIN order_pizza OP ON O.id = OP.order_id"
                        " LEFT JOIN pizza P ON P.id = OP.pizza_id"
                        " GROUP BY P.name"
                        " ORDER BY amount DESC, P.name"
                        " LIMIT 3")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"orderCount":row[0], "pizzaName":row[1]})

        return response