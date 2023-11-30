""" This drives a webapp to present the user with a form to generate
    a madlibs story. """

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story as story_instance

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def show_prompts_form():
    """ Show a form to ask the user for inputs for the madlibs story. """

    return render_template(
        'questions.html',
        prompts=story_instance.prompts
    )

@app.get('/results')
def show_result_story():
    """ Use form input to display madlibs story."""

    story_to_display = story_instance.get_result_text(request.args)

    return render_template(
        'results.html',
        story_to_display = story_to_display
    )