# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=100)])
    submit = SubmitField('ingresar')

class PersonalForm(FlaskForm):
    name = StringField('nombre', validators=[DataRequired()])
    title = StringField('titulo', validators=[DataRequired()])
    phone = StringField('telefono')
    email = StringField('email')
    linkedin = StringField('linkedin')
    github = StringField('github')
    about = TextAreaField('sobre_mi')
    submit = SubmitField('guardar')
