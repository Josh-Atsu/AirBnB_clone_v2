#!/usr/bin/python3
"""
starts a Flask web application
web application is listening on 0.0.0.0, port 5000
"""
from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """Display <Hello HBNB!>"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """display HBNH"""
    return "HBNB"


@app.route("/c/<text>")
def c_name(text):
    """display “C ” followed by the
    value of the text variable"""
    a_text = escape(text)
    r_text = a_text.replace('_', ' ')
    return "C {}".format(r_text)


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """display “Python ”, followed by the value of the text variable
    default value of text is "is cool"
    """
    a_text = escape(text)
    r_text = a_text.replace('_', ' ')
    return "Python {}".format(r_text)


@app.route("/python", strict_slashes=False)
def python_2():
    """display “Python ”, followed by the value of the text variable
    default value of text is "is cool"
    """
    return "Python is cool"


@app.route("/number/<int:n>")
def number(n):
    """display n only if n is an integer"""
    return "{} in a number".format(escape(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
