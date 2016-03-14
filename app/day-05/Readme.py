Flask学习 pip安装多个软件 pip install -r softs.txt Day-00 1,创建'hello,world' 2,创建静态路由 @app.route('/user/<name>') def user(name):
    return 'hello, {name}'.format(name=name)

3,掌握最基本框架
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello'
if __name__ == '__main__':
    app.run()

Day-01
pip install flask-script
1,响应请求,request
from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return user_agent
if __name__ == '__main__':
    app.run()

2,flask-script是通过命令行参数传递配置选项
python hello.py runserver --host 0.0.0.0

Day-02
1,模板的使用 render_template
from flask import render_template
模板放置在templates下
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
#templates/user.html
    <h1>Hello, {{name}}</h1>
模板中变量可加参数
{{name|capitalize}}

#if 条件语句在模板中的使用
{% if user %}
    Hello, {{user}}
{% else %}
    Hello, Stranger
{% endif %}

Day-03
pip install flask-bootstrap
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#templates 下准备base.html,user.html,index.html

Day-04
url_for()函数

Day-05
pip install flask-wtf
flask-wtf 处理web表单获得更愉快体验,(已封装了WTForms包)
