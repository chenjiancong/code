#  all the imports
from __future__ import with_statement
import MySQLdb
from MySQLdb.cursors import DictCursor
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash
from flask.ext.bootstrap import Bootstrap

#  configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123'

#  create our little application :)
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(__name__)
app.config.from_envvar('FLASK_SETTINGS', silent=True)

def connect_db():
    dbconnect = MySQLdb.connect(user='root',
                                passwd='cjcdb',
                                db='flaskr',
                                host='localhost')
    return dbconnect

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'd', None)
    if db is not None:
        db.close()
    g.db.close()

@app.route('/')
def index():
    cur = g.db.cursor(DictCursor)
    query = 'select title, text from entries order by id desc'
    cur.execute(query)
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    #  if not session.get('logged_in'):
        #  abort(401)
    #  cur = g.db.cursors()
    #  cur.execute('insert into entries (title, text) valuse(%s,%s)',
                #  [request.form['title'].encode('utf-8'),request.form['text'].encode('utf-8')])
    #  cur.close()
    #  g.db.commit()
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
