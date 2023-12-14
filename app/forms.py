from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired(), Length(min=3, max=15)])
    password = PasswordField("Password", validators=[
                             InputRequired(), Length(min=6, max=30)])
    submit = SubmitField("Log In")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired(), Length(min=3, max=15)])
    password = PasswordField("Password", validators=[
                             InputRequired(), Length(min=6, max=30)])
    submit = SubmitField("Register")
