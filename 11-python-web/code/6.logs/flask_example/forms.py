from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, URL, Regexp
from wtforms.widgets import TextArea

class QuadraticFormulaForm(FlaskForm):
    a = IntegerField("a", validators=[InputRequired()])
    b = IntegerField("b", validators=[InputRequired()])
    c = IntegerField("c", validators=[InputRequired()])
    submit = SubmitField('Compute')

