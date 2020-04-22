from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, required, Length, optional, Regexp
from wtforms.widgets import PasswordInput

class UserForm(FlaskForm):
    name = StringField('Nimi', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    phone = StringField('Puhelinnumero', [required(), Length(min=5, max=20), Regexp('[0-9]{5,20}')], render_kw={'class':'form-control form-control-sm', 'pattern':'[0-9]{5,20}'})
    address = StringField('Osoite', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    admin = BooleanField('Ylläpitäjä', [optional()], render_kw={'class':'custom-control-input'})
    username = StringField('Käyttäjätunnus', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    password = StringField('Salasana', [required(), Length(min=2, max=50)], widget=PasswordInput(hide_value=False), render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})

    class Meta:
        csrf = False


class UserEditForm(FlaskForm):
    name = StringField('Nimi', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    phone = StringField('Puhelinnumero', [required(), Length(min=5, max=20), Regexp('[0-9]{5,20}')], render_kw={'class':'form-control form-control-sm', 'pattern':'[0-9]{5,20}'})
    address = StringField('Osoite', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    admin = BooleanField('Ylläpitäjä', [optional()], render_kw={'class':'custom-control-input'})
    username = StringField('Käyttäjätunnus', [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
    password = StringField('Salasana', [required(), Length(min=2, max=50)], widget=PasswordInput(hide_value=False), render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})

    class Meta:
        csrf = False