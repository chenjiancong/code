from flask import Flask, request, render_template, jsonify, json
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:cjcdb@localhost/flaskr'
db = SQLAlchemy(app)

class session(db.Model):
    __tablename__ = 'entries'
    id= db.Column(db.String(100), primary_key = True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(100))

@app.route('/scan/<id>', methods=['GET'])
def scan(id):
    result = session.query.filter_by(id=id).first()
    if result is None:
        json_result={'id':None}
        return json.dumps(json_result, ensure_ascii=False)
    else:
        json_result = {'id': result.id, 'title': result.title, 'text': result.text}
        return json.dumps(json_result, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
