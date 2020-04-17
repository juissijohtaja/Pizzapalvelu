from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, SelectField, RadioField
from wtforms.validators import InputRequired, required, Length, optional, NumberRange
from application.orders.models import Order
from application.pizzas.models import Pizza

class OrdersForm(FlaskForm):
    delivery = RadioField('Toimitustapa', [required()], choices=[('kuljetus','Kuljetus'),('nouto','Nouto'),('paikan päällä','Paikan päällä')])
    class Meta:
        csrf = False

class OrdersEditForm(FlaskForm):
    #delivery = StringField('Toimitustapa', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    delivery = RadioField('Toimitustapa', [required()], choices=[('kuljetus','Kuljetus'),('nouto','Nouto'),('paikan päällä','Paikan päällä')])
    received = BooleanField('Vastaanotettu', [optional()], render_kw={'class':'custom-control-input'})
    delivered = BooleanField('Toimitettu', [optional()], render_kw={'class':'custom-control-input'})

    class Meta:
        csrf = False