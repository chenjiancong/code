from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin, BaseView, expose
from flask_admin.contrib import sqla

app = Flask(__name__)
db = SQLAlchemy(app)
admin = Admin(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/web12306'

class Web12306(db.Model):
    __tablename__ = 'web12306'
    user_email = db.Column(db.String(20))
    user_pass  = db.Column(db.String(20))
    user_name  = db.Column(db.String(20))
    user_id    = db.Column(db.Integer, primary_key = True)
    user_nic   = db.Column(db.String(20))
    user_phone = db.Column(db.Integer)

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('hello.html')

admin.add_view(MyView(name = 'hello', endpoint = 'test1', category = 'AA'))
admin.add_view(MyView(name = 'hello', endpoint = 'test2', category = 'AA'))

class MyView2(BaseView):
    @expose('/')
    def index(self):
        return self.render('hello.html')

admin.add_view(MyView2(name = 'Hello'))

class User(sqla.ModelView):
    column_display_pk = True
    form_columns = ['user_email', 'user_pass', 'user_name',
                    'user_id', 'user_nic', 'user_phone']

admin.add_view(User(Web12306, db.session))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
