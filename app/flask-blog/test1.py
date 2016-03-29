from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import  StringField, PasswordField, SubmitField
from wtforms.validators import Required, EqualTo, DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'

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
        return 'Hello'
    return render_template('register.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
