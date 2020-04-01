from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class PizzasForm(FlaskForm):
    name = StringField('Nimi', [validators.Length(min=2)])
    price = IntegerField('Hinta', [validators.required()])
 
    class Meta:
        csrf = False