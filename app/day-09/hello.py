from flask import Flask, render_template,request, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

USERNAME = 'admin'
PASSWORD = '123'

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Something strings'
app.config.from_object(__name__)
app.config.from_envvar('Flask_setting', silent=True)

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')

class RegForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('password', validators=[DataRequired(), EqualTo('password', 'Password not match')])
    submit = SubmitField('submit')

@app.route('/reg', methods = ['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        return 'Your {reg_info}'.format(reg_info=form.data)
    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data != app.config['USERNAME']:
            flash('username wrong')
        elif form.password.data != app.config['PASSWORD']:
            flash('password wrong')
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template('index.html', name=form.username.data)
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
