from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField, RadioField
from wtforms.validators import InputRequired, required, Length, optional, NumberRange
from application.orders.models import Order
from application.pizzas.models import Pizza

class OrdersForm(FlaskForm):
    delivery = RadioField('Toimitustapa', [required()], choices=[('kuljetus','Kuljetus'),('nouto','Nouto'),('paikan päällä','Paikan päällä')])
    pizza_id = IntegerField('Pizza id', [required(), NumberRange(min=1, max=999)], render_kw={'class':'form-control form-control-sm', 'pattern':'[0-9]{1,3}', 'readonly':'true', 'type':'hidden'})

    class Meta:
        csrf = False

class OrdersEditForm(FlaskForm):
    delivery = RadioField('Toimitustapa', [required()], choices=[('kuljetus','Kuljetus'),('nouto','Nouto'),('paikan päällä','Paikan päällä')])
    received = BooleanField('Vastaanotettu', [optional()], render_kw={'class':'custom-control-input'})
    delivered = BooleanField('Toimitettu', [optional()], render_kw={'class':'custom-control-input'})

    class Meta:
        csrf = False