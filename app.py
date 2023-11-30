from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story as story_instance

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def show_prompts_form():
    """open questions page as initial landing"""

    return render_template(
        'questions.html',
        prompts=story_instance.prompts)

@app.get('/results')
def show_result_story():
    """use form input to display story"""

    story_to_display = story_instance.get_result_text(request.args)

    return render_template(
        'results.html',
        story_to_display = story_to_display
    )