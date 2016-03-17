from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:cjcdb@localhost/user'
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Inteeger, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<user %r>' % self.username
