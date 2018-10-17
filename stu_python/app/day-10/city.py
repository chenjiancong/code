from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'Something strings'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cjcdb@localhost/world'

class World(db.Model):
    __tablename__ = 'City'
    ID = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(10))
    CountryCode = db.Column(db.String(10))
    District = db.Column(db.String(10))
    Population = db.Column(db.String(10))

class Scan(Form):
    id = StringField('City_ID', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = Scan()
    if form.validate_on_submit():
        result = World.query.filter_by(ID = form.id.data).first_or_404()
        return '{id},{city_name},{countrycode},{district},{population}'.format(id = result.ID, city_name = result.Name,
                countrycode = result.CountryCode, district = result.District, population = result.Population)
    return render_template('index3.html', form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
