from application import db

class Topping(db.Model):

    __tablename__ = "topping"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
