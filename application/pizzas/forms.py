from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class PizzasForm(FlaskForm):
    name = StringField('Nimi', [validators.Length(min=2)])
    price = IntegerField('Hinta', [validators.required()])

    topping1 = StringField('Täyte1', [validators.Length(min=2)])
    topping2 = StringField('Täyte2', [validators.Length(min=2)])
 
    class Meta:
        csrf = False