from application import db
from application.models import Base, Name
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text


class Pizza(Base, Name):
    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    toppings = relationship("Topping", secondary="pizza_topping")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_pizzas_with_pineapple():
        stmt = text("SELECT P.id, P.name, T.id, T.name"
                     " FROM pizza P, topping T, pizza_topping PT"
                     " WHERE P.id = PT.pizza_id AND T.id = PT.topping_id"
                     " GROUP BY P.id, T.id"
                     " HAVING T.name = 'ananas'")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
