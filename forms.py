# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=100)])
    submit = SubmitField('Ingresar')

class PersonalForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    title = StringField('Titulo', validators=[DataRequired()])
    phone = StringField('Telefono')
    email = StringField('Email')
    linkedin = StringField('Linkedin')
    github = StringField('Github')
    about = TextAreaField('Sobre mi')
    submit = SubmitField('Guardar')
