from flask import Flask, render_template, flash, redirect, url_for, flash, session
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField, SubmitField, TextAreaField
from wtforms.validators import Required

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

class EditForm(Form):
    email = StringField('Email', validators = [Required()])
    username = StringField('Username', validators = [Required()])
    about_me = TextAreaField('About me', validators = [Required()])
    submit = SubmitField('Submit')

class Users(db.Model):
    __tablename__ = 'Users'
    uid = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    about_me = db.Column(db.String(50))
    member_since = db.Column(db.DateTime())

@app.route('/auth/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
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
            #  return redirect(url_for('index'))
    return render_template('login.html', form = form)

@app.route('/auth/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/user/<username>', methods = ['GET', 'POST'])
def user(username):
    form = EditForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        user.email = form.email.data
        user.username = form.username.data
        user.about_me = form.about_me.data
        db.session.add(user)
        return 'hello'
    form.email = Users.email
    form.username = Users.username
    form.password = Users.password
    form.about_me = Users.about_me
    return render_template('edit_profile.html', form = form)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
