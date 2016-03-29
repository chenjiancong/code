from flask import Flask, render_template, flash,redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import EmailField, StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'

class LoginForm(Form):
    email = EmailField('Email', validators = [DataRequired()], id = 'email')
    password = PasswordField('Password', validators = [DataRequired()], id = 'password')
    remember_me = BooleanField('Remember me', validators = [DataRequired()], id = 'remember_me')
    submit   = SubmitField('Log In', validators = [DataRequired()], id = 'sumbit')

class Register(Form):
    email = StringField('Email', validators = [Required()])
    username = StringField('Username', validators = [Required()])
    password = PasswordField('Password', validators = [Required()])
    password2 = PasswordField('Comfirm password',
            validators = [Required(), EqualTo('password', message = 'Password not match')])
    submit = SubmitField('Register', validators = [Required()])

@app.route('/auth/register', methods = ['GET', 'POST'])
def reg():
    form = Register()
    if form.validate_on_submit():
        pass
    return render_template('register.html', form = form)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth/login', methods = ['GET', 'POST'])
def login():
    username = None
    form = LoginForm()
    #  if form.validate_on_submi():
    return render_template('login2.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
