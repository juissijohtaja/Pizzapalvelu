from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, required, Length, optional, NumberRange
from application.toppings.models import Topping
from application.pizzas.models import Pizza


class PizzasForm(FlaskForm):
    name = StringField('Nimi', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    price = IntegerField('Hinta, €', [required(), NumberRange(min=0, max=99)], render_kw={'class':'form-control form-control-sm', 'pattern':'[0-9]{1,2}'})

    topping1 = SelectField('Täyte 1', [required(), Length(min=1, max=3)], render_kw={'class':'custom-select'})
    topping2 = SelectField('Täyte 2', [optional(), Length(min=1, max=3)], render_kw={'class':'custom-select'})
    topping3 = SelectField('Täyte 3', [optional(), Length(min=1, max=3)], render_kw={'class':'custom-select'})
    topping4 = SelectField('Täyte 4', [optional(), Length(min=1, max=3)], render_kw={'class':'custom-select'})

    class Meta:
        csrf = False

    def __init__(self, *args, **kwargs):
        super(PizzasForm, self).__init__(*args, **kwargs)

        choices = [("", "Ei täytettä")]
        for topping in Topping.query.order_by(Topping.id).all():
            choices.append((str(topping.id), topping.name))
        self.topping1.choices = choices
        self.topping2.choices = choices
        self.topping3.choices = choices
        self.topping4.choices = choices

class PizzasEditForm(FlaskForm):
    name = StringField('Nimi', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    price = IntegerField('Hinta, €', [required(), NumberRange(min=0, max=99)], render_kw={'class':'form-control form-control-sm', 'pattern':'[0-9]{1,2}'})

    topping1 = SelectField('Täyte 1', [required(), NumberRange(min=1, max=999)], render_kw={'class':'custom-select'}, coerce=int)
    topping2 = SelectField('Täyte 2', [optional(), NumberRange(min=0, max=999)], render_kw={'class':'custom-select'}, coerce=int)
    topping3 = SelectField('Täyte 3', [optional(), NumberRange(min=0, max=999)], render_kw={'class':'custom-select'}, coerce=int)
    topping4 = SelectField('Täyte 4', [optional(), NumberRange(min=0, max=999)], render_kw={'class':'custom-select'}, coerce=int)
 
    class Meta:
        csrf = False

    def __init__(self, *args, **kwargs):
        super(PizzasEditForm, self).__init__(*args, **kwargs)
        choices = [(0, "Ei täytettä")]
        for topping in Topping.query.order_by(Topping.id).all():
            choices.append((topping.id, topping.name))
        self.topping1.choices = choices
        self.topping2.choices = choices
        self.topping3.choices = choices
        self.topping4.choices = choices
