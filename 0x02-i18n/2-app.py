#!/usr/bin/env python3
"""
Flask app that enables
localization
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    babel configuration
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    find specific locale
    from client
    """
    request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    """
    render template
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
