from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators

class UserEditForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
    phone = IntegerField("Puhelinnumero", render_kw={'class':'form-control form-control-sm'})
    address = StringField("Osoite", [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
    username = StringField("Käyttäjätunnus", [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
    password = PasswordField("Salasana", [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
  
    class Meta:
        csrf = False