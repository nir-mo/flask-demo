import os
import Synonyms

unique_id = 0

# maps unique id -> answers
answers = {}

from flask import Flask, render_template, send_from_directory, request
app = Flask(__name__)


@app.route('/js/<path:path>')
@app.route('/<uid>/js/<path:path>')
def send_js(path, uid=0):
    return send_from_directory(os.path.join('static', 'js'), path)


@app.route('/css/<path:path>')
@app.route('/<uid>/css/<path:path>')
def send_css(path, uid=0):
    return send_from_directory(os.path.join('static', 'css'), path)


@app.route('/img/<path:path>')
@app.route('/<uid>/img/<path:path>')
def send_img(path, uid=0):
    print path
    return send_from_directory(os.path.join('static', 'img'), path)


@app.route("/<uid>/", methods=["POST"])
def check_result(uid):
    res = 'answer' in request.form and \
           request.form['answer'] == answers[int(uid)]
    return render_template('resp.html', res=res)

@app.route("/")
def enter():
    global unique_id

    unique_id += 1
    r, a, op = Synonyms.generate_riddle()

    answers[unique_id] = a
    return render_template("index.html", riddle=r, options=op, id=unique_id)


if __name__ == '__main__':
    app.run(debug=True)

