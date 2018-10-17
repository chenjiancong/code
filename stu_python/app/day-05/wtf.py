from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='SOMETHING STRINGS'

class MyForm(Form):
    name = TextField('name', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return 'Your name is {name}'.format(name=form.data)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
