#!/usr/bin/env python3
"""
This module contains a get_locale function with the babel.localeselector
decorator in a Flask-Babel app to determine locale from request headers
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


class Config(object):
    """Config class for Babel object."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Gets a user based on the 'login_as' parameter"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set the user on `g` before each request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Select the locale based on the user or the request.
    """
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings (if user is logged in)
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Select the timezone based on URL parameter, user setting, or default"""
    # 1. Timezone from URL parameters
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            return pytz.timezone(tz_param).zone
        except UnknownTimeZoneError:
            pass  # Invalid timezone, continue to the next check

    # 2. Timezone from user settings (if user is logged in)
    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user['timezone']).zone
        except UnknownTimeZoneError:
            pass  # Invalid timezone, fallback to default

    # 3. Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def index():
    """Uses GET method to return index.html"""
    user_timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(user_timezone)).strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
