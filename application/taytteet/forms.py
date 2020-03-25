from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TayteForm(FlaskForm):
    name = StringField("Täytteen nimi", [validators.Length(min=2)])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False