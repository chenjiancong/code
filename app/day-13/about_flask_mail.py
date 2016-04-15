from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required
from flask.ext.mail import Mail, Message
from threading import Thread

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'SOMETHINGS'

app.config.update(
#  email settings
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=25,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='username',
    MAIL_PASSWORD='password'
        )

mail =Mail(app)

class Send_Form(Form):
    email = StringField('Recipients Email', validators=[Required()])
    textarea = TextAreaField('Enter Something', validators=[Required()])
    submit = SubmitField('Sent')

def send_async_email(msg):
    mail.send(msg)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Send_Form()
    if form.validate_on_submit():
        msg = Message(subject='Hello',
                        sender = 'username@163.com',
                        recipients=[form.email.data])
        msg.body = 'text body'
        msg.html = form.textarea.data
        thr = Thread(target=send_async_email, args=[msg])
        thr.start()
        mail.send(msg)
        return 'OK'
    return render_template('index1.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
