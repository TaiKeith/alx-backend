#!/usr/bin/env python3
"""
This module contains a basic Flask-Babel app setup.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Config class for Babel object."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localselector
def get_locale():
    """
    Use request.accept_languages to determine the best match with supported
    languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Uses GET method to return 1-index.html"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
