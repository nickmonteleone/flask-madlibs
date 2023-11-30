""" This drives a webapp to present the user with a form to generate
    a madlibs story. """

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

story_options = {
    'Silly': silly_story,
    'Excited': excited_story
}

@app.get('/')
def show_story_select():
    """ Show a dropdown for user to select which madlibs story to use """

    return render_template(
        'dropdown.html',
        story_options=story_options.keys()
    )

@app.get('/prompts')
def show_prompts_form():
    """ Show a form to ask the user for inputs for the madlibs story. """

    story_option = request.args['story_options']
    story_instance = story_options[story_option]

    return render_template(
        'questions.html',
        prompts=story_instance.prompts,
        story_option=story_option
    )

@app.get('/results/<story_option>')
def show_result_story(story_option):
    """ Use form input to display madlibs story."""

    story_instance = story_options[story_option]
    story_to_display = story_instance.get_result_text(request.args)

    return render_template(
        'results.html',
        story_to_display = story_to_display
    )

@app.post('/new-story')
def create_new_story():
    """ Take the user's input from homepage and create a new instance of
        a Story object, which is then used as a template for a madlibs story."""

    story_title = request.form['story_title']
    story_text = request.form['story_text']
    print(story_title, story_text)

    story_options[story_title] = story_text

    story_options=story_options.keys()

    return render_template(
        'dropdown.html',
        story_title,
        story_text
    )
