from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, RadioField, SubmitField, IntegerField, \
    TextAreaField, FloatField, MultipleFileField,FileField
from wtforms.validators import DataRequired, Length, Regexp


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
        label="Type",
        validators=[DataRequired('Please specify type')],
        choices=[
            ('0', 'Customer'),
            ('1', 'Staff')
        ]
    )
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired("Enter a username!"),
                    Length(min=4, max=10, message="Length should be 4-10")]
    )
    email = StringField(
        label='Email',
        validators=[DataRequired("Enter an Email!")]
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired("Enter a password!"),
                    Length(min=6, max=20, message="Length should be 6-20"),
                    # 查下这个啥意思？
                    Regexp("^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$", message="Should have a digit and a letter")]
    )
    password2 = PasswordField(
        label='Repeat Password',
        validators=[DataRequired("Double check your password")]
    )
    image = FileField('The image of the User avatar',
                              validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg', 'jfif'])])  # 头像
    submit = SubmitField('Register')


# 花的信息表
class FlowerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    detail = TextAreaField('Introduction', validators=[DataRequired()])  # 简介
    price = FloatField('Price', validators=[DataRequired()])  # 单价
    number = IntegerField('Inventory', validators=[DataRequired()])  # 库存
    image = MultipleFileField('The preview of the flower',
                              validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg', 'jfif'])])  # 预览图
    address = StringField('Shop address', validators=[DataRequired()])  # 店铺地址
    submit = SubmitField('Comfirm')


class SearchForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()])


class ChangePasswordForm(FlaskForm):
    passwordold = PasswordField(
        label='Passwordold',
        validators=[DataRequired("Please enter your oldpassword")]
    )

    password = PasswordField(
        label='Password',
        validators=[DataRequired("Enter a password!"),
                    Length(min=6, max=20, message="Length should be 6-20"),
                    # 查下这个啥意思？
                    Regexp("^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$", message="Should have a digit and a letter")]
    )
    password2 = PasswordField(
        label='Repeat Password',
        validators=[DataRequired("Double check your password")]
    )
    submit = SubmitField('submit')


class CheckoutForm(FlaskForm):
    firstname = StringField('FirstName', validators=[DataRequired()])
    lastname = StringField('LastName', validators=[DataRequired()])
    streetaddress = StringField('Street address', validators=[DataRequired()])  # 店铺地址
    phone = StringField('Contact phone', validators=[DataRequired()])
    notes = StringField('notes', validators=[DataRequired()])
    submit = SubmitField('Proceed to checkout')
