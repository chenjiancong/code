from flask import Flask, render_template, flash, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Required
from flask.ext.login import login_user

USERNAME = 'admin'
PASSWORD = '123'

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
        #  if form.username.data != app.config['USERNAME']:
            #  flash('wrong')
        #  elif form.password.data != app.config['PASSWORD']:
            #  flash('wrong')
        #  else:
            #  flash('logged')
            #  return 'hello'
        user = Users.query.filter_by(username=form.username.data).first()
        if form.username.data != user.username:
            flash('username wrong')
        elif form.password.data != user.password:
            flash('password wrong')
        else:
            return 'hello'
    return render_template('login3.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
