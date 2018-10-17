from flask import Flask
from flask.ext.wtf import Form
from wtforms import StringField,TextAreaField, SubmitField, PasswordField
from wtforms.validators import Required

class Send_email(Form):
    email = StringField('Email', validators = [Required()])
    text = TextAreaField('Text', validators = [Required()])
    submit = SubmitField('Submit')

class Login(Form):
    username = StringField('Username', validators = [Required()])
    password = PasswordField('Password', validators = [Required()])
    submit = SubmitField('Submit')



