#!/usr/bin/env python3
"""1. Basic Babel setup
"""

from flask import Flask, render_template

from flask_babel import Babel


class Config():
    """config for the flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@app.route("/")
def hello_world():
    return render_template('1-index.html')
