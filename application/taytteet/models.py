from application import db

class Tayte(db.Model):

    __tablename__ = "topping"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    #done = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        #self.done = False
