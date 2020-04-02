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


