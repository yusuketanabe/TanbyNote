from flask import Flask, render_template, abort, request
from note.database import Memo, db_session, init_db
from datetime import datetime, date

app = Flask(__name__)

init_db() # database initialize command

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def home():
    contents = Memo.query.all()
    return render_template('index.html', contents=contents)

@app.route('/<title>', methods=['GET'])
def page(title):
    content = Memo.query.filter_by(title=title).first()
    if content is None:
        abort(404)
    return render_template('page.html', content=content)

@app.route('/<title>', methods=['POST']) # pattern 2, post data used 'httpie'
def post_content(title=None):
    if title is None:
        abort(404)
    content = Memo.query.filter_by(title=title).first()
    if content is None:
        content = Memo(title, request.form['body'])
    else:
        content.body = request.form['body']
        content.date = datetime.now().strftime('%Y-%m-%d %H:%M')
    db_session.add(content)
    db_session.commit()
    return content.body

app.run(port=5000) # debug=False
