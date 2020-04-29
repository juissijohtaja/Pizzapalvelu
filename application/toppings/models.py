from application import db
from application.models import Base, Name
from sqlalchemy.orm import relationship

class Topping(Base, Name):
    __tablename__ = "topping"

    pizzas = relationship("Pizza", secondary="pizza_topping")

    def __init__(self, name):
        self.name = name
