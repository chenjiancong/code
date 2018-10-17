from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/user/<name>')
def user(name):
    return 'Hello, {name}'.format(name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
