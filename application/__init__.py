# flask-application
from flask import Flask
app = Flask(__name__)

# database connectivity and ORM
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizzapalvelu.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# login functionality
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

# load application content
from application import views

from application.toppings import models
from application.toppings import views

from application.pizzatoppings import models

from application.pizzas import models
from application.pizzas import views

from application.orderpizzas import models

from application.orders import models
from application.orders import views

from application.users import views

from application.auth import models
from application.auth import views

# login functionality, part 2
from application.auth.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# database creation
try: 
    db.create_all()
except:
    pass