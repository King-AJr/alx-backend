#!/usr/bin/env python3
"""
Basic flask app
rendering a simple
html template
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    render html template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port=8080)
