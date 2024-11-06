#!/usr/bin/env python3
"""
This module contains a get_locale function with the babel.localeselector
decorator in a Flask-Babel app to determine locale from request headers
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config class for Babel object."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Use request.accept_languages to determine the best match with supported
    languages.
    """
    # Check if the 'locale' parameter is in the query string and is valid
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Fall back to the best match from 'Accept-Language' headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Uses GET method to return 4-index.html"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
