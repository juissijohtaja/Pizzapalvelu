from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class ToppingsForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
 
    class Meta:
        csrf = False