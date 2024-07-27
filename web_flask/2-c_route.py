#!/usr/bin/python3
"""
starts a Flask web application
web application is listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
