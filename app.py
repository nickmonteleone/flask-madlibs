from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def open_questions():
    """open questions page as initial landing"""

    return render_template(
        'questions.html',
        prompts=silly_story.prompts)

@app.get('/results')
def show_result_text():
    """use form input to display text"""