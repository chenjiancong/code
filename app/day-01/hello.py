from flask import Flask, request
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return 'Hello,{name}\n <p>Your browser is {browser}'.format(name=name, browser=user_agent)

if __name__ == '__main__':
    manager.run()
