from flask import Flask, render_template, request, jsonify, json, redirect, url_for
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

class session(db.Model):
    __tablename__ = 'student'
    stu_id = db.Column(db.String(10), primary_key = True)
    name   = db.Column(db.String(10))
    cla_id = db.Column(db.String(10))

class Scan(Form):
    stu_id = StringField('Stu_id', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])


@app.route('/scan/<stu_id>', methods = ['GET'])
def scan1(stu_id):
    result = session.query.filter_by(stu_id=stu_id).first()
    if result is None:
        json_result={'stu_id':None}
        return json.dumps(json_result, ensure_ascii=False)
    else:
        json_result = {'stu_id': result.stu_id, 'name': result.name, 'cla_id': result.cla_id}
        return json.dumps(json_result, ensure_ascii=False)

@app.route('/', methods =['GET', 'POST'])
def scan():
    form =  Scan()
    if form.validate_on_submit():
        result = session.query.filter_by(stu_id=form.stu_id.data).first_or_404()
        #  return redirect(url_for('show_stu_id'))
        return 'stu_id is {stu_id}, name:{name}, {cla_id}'.format(stu_id=result.stu_id, name=result.name, cla_id=result.cla_id)
    return render_template('index3.html', form=form)

@app.route('/s/<stu_id>', methods=['GET'])
def show_stu_id(stu_id):
    #  stu_id = session.query.filter_by(stu_id=stu_id).first_or_404()
    pass
    #  result = session.query.filter_by(stu_id=stu_id).first()
    #  return 'stu_id is {stu_id}, name:{name}, {cla_id}'.format(stu_id=result.stu_id, name=result.name, cla_id=result.cla_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
