from flask import Flask, render_template, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import  StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required, EqualTo, DataRequired
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/flaskr'

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

class Register(Form):
    email = StringField('Email', validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Comfirm password', validators =
                            [DataRequired(), EqualTo('password', message = 'Password not match')])
    submit = SubmitField('Register', validators = [DataRequired()])

@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can login')
        return 'Hello {username}'.format(username=form.username.data)
    return render_template('register.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
