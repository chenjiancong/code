from flask import Flask,session, render_template, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'Something Strings'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/web12306'

class MyForm(Form):
    user_id = StringField('Name', validators = [DataRequired()])
    submit = SubmitField('Submit', validators = [DataRequired()])

class Web12306(db.Model):
    __tablename__ = 'web12306'
    user_email = db.Column(db.String(20))
    user_pass = db.Column(db.String(10))
    user_name = db.Column(db.String(20))
    user_id = db.Column(db.Integer, primary_key = True)
    user_nic = db.Column(db.String(20))
    user_phone = db.Column(db.Integer)

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        result = Web12306.query.filter_by(user_id = form.user_id.data).first_or_404()
        return '{email},{user_pass},{name},{user_id},{nic},{phone}'.format(email=result.user_email, user_pass = result.user_pass,
                name = result.user_name, user_id = result.user_id, nic = result.user_nic, phone = result.user_phone
                )
        #  session['name'] = form.name.data
        #  return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
