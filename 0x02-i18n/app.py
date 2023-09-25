#!/usr/bin/env python3
"""
Flask app that enables
localization
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from pytz import timezone
import pytz.exceptions
from datetime import datetime
import locale


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
    if g.user:
        if g.user.get('locale') in Config.LANGUAGES:
            return g.user.get('locale')


def get_user():
    if "login_as" in request.args:
        id = request.args.get('login_as')
        return users.get(int(id))
    else:
        return None

@app.before_request
def before_request() -> None:
    user = get_user()
    g.user = user
    print('here')
    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    time_format = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(time_format)
    print(g.time)
    

@babel.timezoneselector
def get_timezone():
    user_timezone = request.args.get('timezone', None)
    if user_timezone:
        try:
            return timezone(user_timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            user_timezone = g.user.get('timezone')
            return timezone(user_timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    default_timezone = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_timezone
    

@app.route("/")
def index():
    """
    render template
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0", debug=True)
