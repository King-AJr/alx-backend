#!/usr/bin/env python3
"""
Flask app that enables
localization
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    print('in get user')
    if "login_as" in request.args:
        id = request.args.get('login_as')
        return users.get(int(id))
    else:
        return None

@app.before_request
def before_request() -> None:
    user = get_user()
    g.user = user
    


@app.route("/")
def index():
    """
    render template
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0", debug=True)
