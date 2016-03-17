from flask import Flask, request, session, render_template, flash, url_for, redirect
from flask.ext.bootstrap import Bootstrap

#  configure
DEBUG = True
SECRET_KEY = 'DEVELOMENT APP'
USERNAME = 'admin'
PASSWORD = '123'

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTINGS', silent=True)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('Wrong Username')
            error = 'Wrong username'
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Wrong Password')
            error = 'Your password is Wrong'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('user', name=USERNAME))
    return render_template('login.html', error = error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged_out')
    return redirect(url_for('index'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')

