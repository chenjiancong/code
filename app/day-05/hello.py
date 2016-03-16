from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

#  configuration
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
USERNAME = 'admin'
PASSWORD = '123'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.form['username'] != app.config['USERNAME']:
        error = 'Invalid username'
    elif request.form['password'] != app.config['PASSWORD']:
        error = 'Invalid password'
    else:
        session['logged_in'] = True
        flash('You were logged in')
    return render_template('login.html', error=errop)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
