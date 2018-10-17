from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello</h1>'

@app.route('/user/<name>')
def name(name):
    return '<h1>Hello, {user_name}</h1>'.format(user_name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
