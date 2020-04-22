from application import db
from application.models import Base, Name
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text

class Pizza(Base, Name):
    price = db.Column(db.Integer, nullable=False)

    toppings = relationship("Topping", secondary="pizza_topping")
    orders = relationship("Order", secondary="order_pizza")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_pizzas_with_pineapple():
        stmt = text("SELECT P.id, P.name, T.id, T.name"
                        " FROM pizza P, topping T, pizza_topping PT"
                        " WHERE P.id = PT.pizza_id AND T.id = PT.topping_id"
                        " GROUP BY P.id, T.id"
                        " HAVING T.name = 'ananas'"
                        " LIMIT 3")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "topping":row[3]})

        return response
    
    @staticmethod
    def find_pizzas_with_chili():
        stmt = text("SELECT P.id, P.name, T.id, T.name"
                        " FROM pizza P, topping T, pizza_topping PT"
                        " WHERE P.id = PT.pizza_id AND T.id = PT.topping_id AND T.name IN ('chili', 'jalapeno')"
                        " GROUP BY P.id, T.id")
        res = db.engine.execute(stmt)

        response = []
        seen_titles = set()
        for row in res:
            if row[1] not in seen_titles:
                response.append({"id":row[0], "name":row[1]})
                seen_titles.add(row[1])

        return response
