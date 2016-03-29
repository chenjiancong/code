from flask import Flask, render_template, flash, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/flaskr'

class LoginForm(Form):
    username = StringField('Username', validators = [Required()])
    password = PasswordField('Password', validators = [Required()])
    submit = SubmitField('Login', validators = [Required()])

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

@app.route('/auth/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login3.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
