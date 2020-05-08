from application import db
from application.models import Base, Name

class User(Base, Name):

    __tablename__ = "account"
  
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, unique=False, default=False)

    orders = db.relationship('Order', backref='account', lazy=True, cascade="all, delete-orphan")


    def __init__(self, name):
        self.name = name
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(self):
        if (self.admin == True):
            return ["ADMIN"]
        else:
            return ["USER"]