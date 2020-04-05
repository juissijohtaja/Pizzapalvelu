from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class ToppingsForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
 
    class Meta:
        csrf = False

class ToppingsEditForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)], render_kw={'class':'form-control form-control-sm'})
 
    class Meta:
        csrf = False