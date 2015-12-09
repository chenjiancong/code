#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# all the imports
from __future__ import with_statement
import MySQLdb
from MySQLdb.cursors import DictCursor
from contextlib import closing
from flask import Flask, request, session, g, redirect,url_for, \
        abort, render_template, flash

# comfiguration
DEBUG = True
SECRET_KEY = 'development key'
USRENAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    db = MySQLdb.connect(user='root',
                         passwd='cjcdb',
                         db='webdb',
                         host='localhost')
    return db

@app.before_request
def before_request():
    g.db = connect_db()

#@app.teardown_request
#def teardown_request(exception):
#    db = getattr(g, 'db', None)
#    if db is not None:
#        db.close()
#    g.db.close()

@app.after_request
def after_request(response):
    """Closes the database again at the end of the request."""
    g.db.close()
    return response

@app.route('/')
def show_entries():
    cur = g.db.cursor(DictCursor)
    query = 'select title, text from entries order by id desc'
    cur.execute(query)
    entries = [dict(title=row['title'].decode('utf-8'), text=row['text'].decode('utf-8')) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

#@app.route('/add', methods=['POST'])
#def add_entry():
#    if not session.get('logged_in'):
#        abort(401)
#    g.db.execute('insert into entries (title, text) values (?, ?)'
#                [request.form['title'].encode('utf-8'), request.form['text'].endcode('utf-8')])
#    g.db.commit()
#    flash('New entry was successfully posted')
#    return rediect(url_for('show_entries'))

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
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

#@app.route('/logout')
#def logout():
#    session.pop('logged_in', None)
#    flash('You were logged out')
#    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
