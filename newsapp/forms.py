from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, DateField, SubmitField, TimeField, IntegerField, \
	TextAreaField, SelectMultipleField, FileField, FloatField
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
	type = RadioField(
		label = "Type",
		validators = [DataRequired('Please specify type')],
		choices = [
			('0', 'Customer'),
			('1', 'Staff')
		]
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

# 花的信息表
class FlowerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    detail = TextAreaField('Introduction', validators=[DataRequired()]) # 简介
    price = FloatField('Price', validators=[DataRequired()]) # 单价
    number = IntegerField('Inventory', validators=[DataRequired()]) # 库存
    image = FileField('The preview of the flower', validators=[FileAllowed(['jpg','png','gif','jpeg','jfif'])]) # 预览图
    address = StringField('Shop address', validators=[DataRequired()]) # 店铺地址
    submit = SubmitField('Comfirm')


