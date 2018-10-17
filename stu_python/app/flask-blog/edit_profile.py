from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/flaskr'

class EditForm(Form):
    name = StringField('Username', validators = [Required()])
    password = PasswordField('PasswordField', validators = [Required()])
    about_me = TextAreaField('About_me', validators = [Required()])
    submit = SubmitField('Submit', validators = [Required()])

class Users(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    about_me = db.Column(db.Text())

@app.route('/edit-profile', methods = ['GET', 'POST'])
def edir_profile():
    form = EditForm()
    if form.validate_on_submit():
        current_Users.username = form.username.data
        current_Users.password = ''
        current_Users.about_me = form.about_me.data
        db.session.add(current_Users)
        flash('Your profile has been updated.')
        return 'Hello'
    form.username = current_Users.username
    form.password = current_Users.password
    form.about_me = current_Users.about_me
    return render_template('edit_profile.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
