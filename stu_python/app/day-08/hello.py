from flask import Flask, render_template
from flask.ext.admin import Admin
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

admin = Admin(app, name='jack', template_mode='bootstrap2')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
