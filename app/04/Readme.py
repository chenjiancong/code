Day-01
重新编写,登录页

Day-02
1,index页显示文章
2,添加footer
3,微调了一下index显示页

Day-03
pass

Day-04
flask-login使用
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.lovin_view = 'signin' #登录视图
login_manager.login_message = u'Please Sign In' #登录提示信息

class User(db.Model):
    ...
    ...
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.uid)

    def is_anonymous(self):
        return False

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route('/signin', methods = ['GET', 'PPST'])
def signin():
    ...
    ...
    login_user(user)

@app.route('/manage')
@login_required  #在需要登录验证的地方添加
def manage():
    return ...

@app.route('/signout')
def signout():
    ...
    ...
    logout_user()
