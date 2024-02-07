#!/usr/bin/env python3
"""1. Basic Babel setup
"""

from flask import Flask, render_template, request, g
from babel import dates
import pytz
from babel.timezones import get_timezone as babel_get_timezone
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
    lang = 'en'
    tmp_lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    if tmp_lang:
        lang = tmp_lang
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        lang = g.user['locale']
    tmp_lang = request.args.get('locale')
    if tmp_lang in app.config['LANGUAGES']:
        lang = tmp_lang

    return lang



def validate_timezone(timezone) -> bool:
    try:
        pytz.timezone(timezone)
        return True
    except pytz.UnknownTimeZoneError:
        return False

@dates.timezoneselector
def get_timezone() -> str:
    """get utc"""
    timezone_from_url = request.args.get('timezone')

    if timezone_from_url and validate_timezone(timezone_from_url):
        return timezone_from_url

    user_timezone = None
    if g.user and validate_timezone(g.user['timezone']):
        user_timezone = g.user['timezone']

    if user_timezone and validate_timezone(user_timezone):
        return user_timezone

    return 'UTC'


@app.route("/")
def hello_world() -> str:
    """this is a route"""
    username = None
    if g.user:
        print(g.user)
        username = g.user['name']
    current_timezone = get_timezone()
    return render_template('7-index.html', username=username, timezone=current_timezone)
