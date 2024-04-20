from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "IMMMA"
app.config["DEBUG"] = True

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False #or True

@app.route("/", methods=["GET"])
def home():
  prompts = story.prompts
  return render_template("form.html", prompts=prompts)

@app.route("/story", methods=["POST"])
def show_story():
  answers = {prompt: request.form[prompt] for prompt in story.prompts}
  result_story = story.generate(answers)
  return render_template("story.html", story=result_story)