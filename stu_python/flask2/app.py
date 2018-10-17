#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username =='aa' and password=='11':
        return render_template('login_ok.html',username=username)
    return render_template('login_form.html',message='Bad username or password')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
