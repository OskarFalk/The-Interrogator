from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    mail = StringField('mail', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('register')

class QuesteningForm(FlaskForm):
    Question1 = SelectField('Question 1', validators=[DataRequired()], choices=('Chocolate', 'Vanilla', 'CookieDough'))
    Question2 = SelectField('Question 2', validators=[DataRequired()], choices=('Letmilk', 'Sødmilk', 'Minimilk', 'Skummilk'))
    Question3 = SelectField('Question 3', validators=[DataRequired()], choices=('Pizza', 'Burger', 'cookieDough', 'Other'))
    Question4 = SelectField('Question 4', validators=[DataRequired()], choices=('Cash', 'Card', 'ApplePay', 'GooglePay', 'Mobile Pay'))
    Question5 = SelectField('Question 5', validators=[DataRequired()], choices=('Moody', 'Happy', 'Sad', 'I DONT KNOW', 'im not quite sure'))
    UserID = StringField('UserID')
    submit = SubmitField('answer')

