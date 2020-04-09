from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, required, Length, optional
from application.toppings.models import Topping


class PizzasForm(FlaskForm):
    name = StringField('Nimi', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    price = IntegerField('Hinta', [required()], render_kw={'class':'form-control form-control-sm'})

    topping1 = SelectField('Täyte 1', [required()], render_kw={'class':'custom-select'}, coerce=int)
    topping2 = SelectField('Täyte 2', render_kw={'class':'custom-select'}, coerce=int)
    topping3 = SelectField('Täyte 3', render_kw={'class':'custom-select'}, coerce=int)
    topping4 = SelectField('Täyte 4', render_kw={'class':'custom-select'}, coerce=int)

    class Meta:
        csrf = False

    def __init__(self, *args, **kwargs):
        super(PizzasForm, self).__init__(*args, **kwargs)

        choices = [(0, "Valitse täyte")]
        for topping in Topping.query.order_by(Topping.id).all():
            choices.append((topping.id, topping.name))
        self.topping1.choices = choices
        self.topping2.choices = self.topping1.choices
        self.topping3.choices = self.topping1.choices
        self.topping4.choices = self.topping1.choices

class PizzasEditForm(FlaskForm):
    name = StringField('Nimi', [Length(min=2)], render_kw={'class':'form-control form-control-sm'})
    price = IntegerField('Hinta', [required()], render_kw={'class':'form-control form-control-sm'})
    infoText = {'placeholder': 'Täytteen numero', 'class':'form-control form-control-sm'}

    topping1 = IntegerField('Täyte 1', [required()], render_kw=infoText)
    topping2 = IntegerField('Täyte 2', [optional()], render_kw=infoText)
    topping3 = IntegerField('Täyte 3', [optional()], render_kw=infoText)
    topping4 = IntegerField('Täyte 4', [optional()], render_kw=infoText)
 
    class Meta:
        csrf = False