#!/usr/bin/env python3
"""
This module contains a get_locale function with the babel.localeselector
decorator in a Flask-Babel app to determine locale from request headers
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


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
    # Check if the user is logged in and has a preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    # Fall back to the best match from 'Accept-Language' headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Uses GET method to return 5-index.html"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
