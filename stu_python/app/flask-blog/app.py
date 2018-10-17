from flask import Flask, render_template, flash, redirect, url_for, flash, session
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Required, DataRequired, EqualTo

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/flaskr'
app.config.from_object(__name__)
app.config.from_envvar('Flask_setting', silent=True)

class LoginForm(Form):
    username = StringField('Username', validators = [Required()])
    password = PasswordField('Password', validators = [Required()])
    submit = SubmitField('Login', validators = [Required()])

class Users(db.Model):
    __tablename__ = 'Users'
    uid = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

@app.route('/auth/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data,email=form.email.data).first()
        if form.username.data != user.username:
            flash(' wrong username')
            error = 'Invalid username'
        elif form.password.data != user.password:
            flash(' wrong password')
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were Logged in ')
            return redirect(url_for('index'))
    return render_template('login.html', form = form)

@app.route('/auth/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

class Register(Form):
    email = StringField('Email', validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Comfirm password', validators =
                            [DataRequired(), EqualTo('password', message = 'Password not match')])
    submit = SubmitField('Register', validators = [DataRequired()])

@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        register = Users.query.filter_by(username=form.username.data,email=form.email.data).first()
        if form.username.data == register.username:
            flash('Have same username')
            error = 'Invalid username'
        elif form.email.data == register.email:
            flash('Have same email')
            error = 'Invalid email'
        else:
            user = Users(email = form.email.data,
                        username = form.username.data,
                        password = form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('You can login')
            return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
