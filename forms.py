from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BoldifyEncryptForm(FlaskForm):
    boldMessage = StringField('Bolded Message: ',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')   