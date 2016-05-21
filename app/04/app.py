from flask import Flask,request, render_template, flash, session, url_for, redirect
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'signin'
#  login_manager.login_message = u'Please Sign In'

app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/flaskr'
app.config['SECRET_KEY'] = 'SOMETYHING STRING'

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.uid)

    def is_anonymous(self):
        return False

class Entries(db.Model):
    __tablename__ = "entries"
    auto_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(50))

    def __init__(self, title, text):
        self.title = title
        self.text = text

@app.route('/')
def index():
    entries = Entries.query.all()
    return render_template('index.html', entries=entries)

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['name']).first()
        if user is None or request.form['name'] != user.username:
            flash('Username or Password Wrong')
        elif request.form['password'] != user.password:
            flash('Username or Password Wrong')
        else:
            session['logged_in'] = True
            login_user(user)

            flash('You were Sign In')
            return redirect(url_for('manage'))
            #  return redirect(url_for('user', name = current_user.username))
            #  return 'Hello'
    return render_template('signin.html', error = error)


@app.route('/signout', methods=['GET'])
def signout():
    session.pop('logged_in', None)
    flash('You were Sign Out')
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/manage')
@login_required
def manage():
    return render_template('manage.html')

@app.route('/user/<name>')
@login_required
def user(name):
    return render_template('user.html', name = name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
