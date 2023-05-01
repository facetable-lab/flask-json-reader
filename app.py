from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.load_candidates_from_server_json()

    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>')
def page_candidate(x):
    candidate = utils.get_candidate(x)

    return render_template('candidate.html', candidate=candidate)


app.run()
