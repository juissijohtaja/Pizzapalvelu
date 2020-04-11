from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField
from wtforms.validators import InputRequired, required, Length, optional

class ToppingsForm(FlaskForm):
    name = StringField("Nimi", [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
 
    class Meta:
        csrf = False

class ToppingsEditForm(FlaskForm):
    name = StringField("Nimi", [required(), Length(min=2, max=50)], render_kw={'class':'form-control form-control-sm', 'pattern':'.{2,50}'})
 
    class Meta:
        csrf = False