from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return render_template('useragent.html', user_agent=user_agent)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
