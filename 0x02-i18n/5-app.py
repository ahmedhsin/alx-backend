#!/usr/bin/env python3
"""1. Basic Babel setup
"""

from flask import Flask, render_template, request, g

from flask_babel import Babel

from typing import Union


class Config():
    """config for the flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """return a user or a none"""

    id = request.args.get('login_as')
    if id:
        id = int(id)
    if id in users:
        return users[id]
    return None


@app.before_request
def before_request() -> None:
    """set g obj"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """get local"""
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world() -> str:
    """this is a route"""
    username = None
    if g.user:
        print(g.user)
        username = g.user['name']
    return render_template('5-index.html', username=username)
