from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object('config')

from app import views, errors, forms, models
