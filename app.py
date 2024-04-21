from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "IMMMA"
app.config["DEBUG"] = True

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False #or True

@app.route("/", methods=["GET"])
def home():
  story_titles = stories.keys()
  return render_template("choose_story.html", story_titles=story_titles)

@app.route("/story", methods=["POST"])
def show_story():
    story_key = request.form['story_key']
    story_instance = stories[story_key]
    answers = {prompt: request.form[prompt] for prompt in story_instance.prompts}
    result_story = story_instance.generate(answers)
    return render_template("story.html", story=result_story)



@app.route("/form", methods=["POST"])
def show_form():
    story_key = request.form['story_choice']
    prompts = stories[story_key].prompts
    return render_template("form.html", prompts=prompts, story_key=story_key)

