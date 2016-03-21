from flask import Flask, render_template, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Something strings'

class RegForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    Password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', 'password not match')])
    submit = SubmitField('Submit')

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        return 'name:{name}, password:{password}'.format(name=form.username.data, password=form.password.data)
    return render_template('reg.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

