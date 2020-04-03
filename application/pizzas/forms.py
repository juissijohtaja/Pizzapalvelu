from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators, SelectField

class PizzasForm(FlaskForm):
    name = StringField('Nimi', [validators.Length(min=2)])
    price = IntegerField('Hinta', [validators.required()])
    infoText = {"placeholder": "Täytteen numero"}

    topping1 = IntegerField('Täyte 1', [validators.required()], render_kw=infoText)
    topping2 = IntegerField('Täyte 2', [validators.optional()], render_kw=infoText)
    topping3 = IntegerField('Täyte 3', [validators.optional()], render_kw=infoText)
    topping4 = IntegerField('Täyte 4', [validators.optional()], render_kw=infoText)
 
    class Meta:
        csrf = False