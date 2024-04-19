from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config["SECRET_KEY"] = "IMMMA"
app.config["DEBUG"] = True

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False #or True

@app.route("/")
def home():
  return "IT'S WORKING YO!"