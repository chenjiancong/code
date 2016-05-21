from flask import render_template
from forms import Send_email
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods = ['GET', 'POST'])
def send_email():
    form = Send_email()
    if form.validate_on_submit():
        return 'OK'
    return render_template('send_email.html', form = form)

@app.route('/forms', methods = ['GET', 'POST'])
def forms():
    form = About_forms()
    return render_template('forms.html', form = form)
