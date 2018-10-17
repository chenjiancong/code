from flask import Flask, render_template, session, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'SOMETHING STRINGS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/school'

class Student(db.Model):
    __tablename__ = 'student'
    stu_id = db.Column(db.Integer, primary_key = True)
    name   = db.Column(db.String(10))
    cla_id = db.Column(db.String(10))

class Scan(Form):
    stu_id = StringField('Stu_id', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])

@app.route('/', methods = ['GET', 'POST'])
def scan():
    stu_id = None
    form = Scan()
    if form.validate_on_submit():
        result = Student.query.filter_by(stu_id=form.stu_id.data).first_or_404()
        return render_template('index3.html', stu_id=result.stu_id, name=result.name, cla_id=result.cla_id, form=form)
        #  session['stu_id'] = form.stu_id.data
        #  return redirect(url_for('show'))
    return render_template('index3.html', form = form)

@app.route('/id/<stu_id>', methods = ['GET', 'POST'])
def show():
    return render_template('index3.html', stu_id = stu_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
