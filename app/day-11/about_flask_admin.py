from flask import Flask
from flask.ext.admin import Admin, BaseView, expose

app = Flask(__name__)
admin = Admin(app, name = 'My App')

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('hello.html')

    @expose('/test')
    def test(self):
        return self.render('hello.html')

admin.add_view(MyView(name = 'Hello 1', endpoint = 'test1', category = 'Test'))
admin.add_view(MyView(name = 'Hello 2', endpoint = 'test2', category = 'Test'))

class aa(BaseView):
    @expose('/')
    def show(self):
        return self.render('hello.html')

admin.add_view(aa(name = 'show'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
