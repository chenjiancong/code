from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import TextAreaField, BooleanField, TextField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

USERNAME = 'admin'
PASSWORD = '123'

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SOMEGHING STRINGS'
app.config.from_object(__name__)
app.config.from_envvar('Flask_settings', silent=True)

class MyForm(Form):
    tname = TextField('tname', validators=[DataRequired()])
    sname = StringField('sname', validators=[DataRequired()])
    textarea = TextAreaField('Somethings', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    Password2 = PasswordField('Comfir password', validators=[DataRequired(), EqualTo('password', 'password not match')])
    submit = SubmitField('Submit')
    accept_tos = BooleanField('I accept the TOS')

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/reg', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return 'you name is {name}'.format(name=form.data)
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data != app.config['USERNAME']:
            flash('Wrong username')
            error = 'Wrong username'
        elif form.password.data != app.config['PASSWORD']:
            flash('Wrong password')
            error = 'Wrong password'
        else:
            session['logged_in'] = True
            flash('Your were logged in')
            return render_template('index.html', name = USERNAME)
    return render_template('login2.html', form = form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
