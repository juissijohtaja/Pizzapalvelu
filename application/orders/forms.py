from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, required, Length, optional, NumberRange
from application.orders.models import Order
from application.pizzas.models import Pizza

class OrdersForm(FlaskForm):
    delivery = StringField('Toimitustapa', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})

    class Meta:
        csrf = False

class OrdersEditForm(FlaskForm):
    delivery = StringField('Toimitustapa', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    received = BooleanField('Vastaanotettu', [optional()], render_kw={'class':'custom-control-input'})
    delivered = BooleanField('Toimitettu', [optional()], render_kw={'class':'custom-control-input'})

    class Meta:
        csrf = False