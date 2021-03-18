from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, DateField, SubmitField,TimeField,IntegerField,TextAreaField,SelectMultipleField,FileField
from wtforms.validators import DataRequired, Length, Regexp,Email
from flask_wtf.file import FileAllowed,FileRequired

class LoginForm(FlaskForm):
	username = StringField(
		label='Username',
		validators=[DataRequired("Please enter your username")],
	)
	password = PasswordField(
		label='Password',
		validators=[DataRequired("Please enter your password")]
	)
	submit = SubmitField('Login')


class SignupForm(FlaskForm):
	username = StringField(
		label='Username',
		validators=[DataRequired("Enter a username!"),
					Length(min=4, max=10,message="Length should be 4-10")]
	)
	email = StringField(
		label='Email',
		validators=[DataRequired("Enter an Email!")]
	)
	password = PasswordField(
		label='Password',
		validators=[DataRequired("Enter a password!"),
					Length(min=6, max=20,message="Length should be 6-20"),
					# 查下这个啥意思？
					Regexp("^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$",message="Should have a digit and a letter")]
	)
	password2 = PasswordField(
		label='Repeat Password',
		validators=[DataRequired("Double check your password")]
	)
	submit = SubmitField('Register')


