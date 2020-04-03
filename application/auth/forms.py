from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
    password = PasswordField("Salasana", [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    phone = IntegerField("Puhelinnumero")
    address = StringField("Osoite", [validators.Length(min=2)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=2)])
    password = PasswordField("Salasana", [validators.Length(min=2)])
  
    class Meta:
        csrf = False