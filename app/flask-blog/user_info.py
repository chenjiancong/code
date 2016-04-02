from flask import Flask, render_template, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/flaskr'
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'

class Users(db.Model):
    __tablename__ = 'Users'
    uid = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    about_me = db.Column(db.String(50))
    member_since = db.Column(db.DateTime())

class EditForm(Form):
    email = StringField('Email', validators = [Required()])
    username = StringField('Username', validators = [Required()])
    about_me = TextAreaField('About me', validators = [Required()])
    submit = SubmitField('Submit')

@app.route('/user/<username>', methods = ['GET', 'POST'])
def user(username):
    user = Users.query.filter_by(username=username).first()
    form = EditForm()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        current_Users.email = form.email.data
        current_Users.username = form.username.data
        current_Users.about_me = form.about_me.data
        db.session.add(current_Users)
        return 'hello'
    form.email = current_Users.email
    form.username = current_Users.username
    form.password = current_Users.password
    form.about_me = current_Users.about_me
    return render_template('edit_profile.html', form = form)



    #  return render_template('user.html',email = user.email, username = username, password = user.password, member_since =
            #  user.member_since)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
