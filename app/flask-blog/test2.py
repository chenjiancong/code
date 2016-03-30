from flask import Flask, render_template, flash,redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, EqualTo

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'

class LoginForm(Form):
    username = StringField('username', validators = [Required()])
    password = PasswordField('Password', validators = [Required()])
    remember_me = BooleanField('Remember me', validators = [Required()])
    submit   = SubmitField('Log In', validators = [Required()])

@app.route('/auth/login', methods = ['GET', 'POST'])
def login():
    username = None
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login3.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
