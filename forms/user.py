from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    burger = StringField('Заказ', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    phone = TextAreaField("Телефоон")
    submit = SubmitField('Войти')