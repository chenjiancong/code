import os
from flask import Flask, render_template
from flask.ext.mail import Mail
from flask.ext.mail import Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

def send_email():
    msg = Message('Email Subject', sender="563439568@qq.com",
                 recipients=['76169288@qq.com'])
    msg.body = 'Hello New user'
    msg.html = '<h1>Email model<h1> body'
    mail.send(msg)
