#!/usr/bin/env python3
"""
Flask app that enables
localization
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    if "locale" in request.args:
        if request.args['locale'] in Config.LANGUAGES:
            return request.args["locale"]
        request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    """
    render template
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(port=8080)
