from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.admin import Admin, BaseView, expose
from flask_admin.contrib import sqla

app = Flask(__name__)
bootstrap = Bootstrap(app)
admin = Admin(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/web12306'

class Web12306(db.Model):
    __tablename__ = 'web12306'
    user_email = db.Column(db.String(20))
    user_pass  = db.Column(db.String(20))
    user_name  = db.Column(db.String(20))
    user_id    = db.Column(db.Integer, primary_key = True)
    user_nic   = db.Column(db.String(20))
    user_phone = db.Column(db.String(20))

class User(sqla.ModelView):
    column_display_pk = True
    form_columns = ['user_email', 'user_pass', 'user_name', 'user_id',
                    'user_nic', 'user_phone']

admin.add_view(User(Web12306, db.session))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
