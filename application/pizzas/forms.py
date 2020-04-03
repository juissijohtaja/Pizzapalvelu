from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators, SelectField

class PizzasForm(FlaskForm):
    name = StringField('Nimi', [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
    price = IntegerField('Hinta', [validators.required()], render_kw={'class':'form-control form-control-sm'})
    infoText = {'placeholder': 'Täytteen numero', 'class':'form-control form-control-sm'}

    topping1 = IntegerField('Täyte 1', [validators.required()], render_kw=infoText)
    topping2 = IntegerField('Täyte 2', [validators.optional()], render_kw=infoText)
    topping3 = IntegerField('Täyte 3', [validators.optional()], render_kw=infoText)
    topping4 = IntegerField('Täyte 4', [validators.optional()], render_kw=infoText)
 
    class Meta:
        csrf = False

class PizzasEditForm(FlaskForm):
    name = StringField('Nimi', [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
    price = IntegerField('Hinta', [validators.required()], render_kw={'class':'form-control form-control-sm'})
    infoText = {'placeholder': 'Täytteen numero', 'class':'form-control form-control-sm'}

    topping1 = IntegerField('Täyte 1', [validators.required()], render_kw=infoText)
    topping2 = IntegerField('Täyte 2', [validators.optional()], render_kw=infoText)
    topping3 = IntegerField('Täyte 3', [validators.optional()], render_kw=infoText)
    topping4 = IntegerField('Täyte 4', [validators.optional()], render_kw=infoText)
 
    class Meta:
        csrf = False