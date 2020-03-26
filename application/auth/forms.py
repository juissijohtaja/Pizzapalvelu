from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=2)])
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    phone = IntegerField("Puhelinnumero")
    address = StringField("Osoite", [validators.Length(min=2)])
    username = StringField("Tunnus", [validators.Length(min=2)])
    password = PasswordField("Salasana", [validators.Length(min=2)])
  
    class Meta:
        csrf = False