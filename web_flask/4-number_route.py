#!/usr/bin/python3
"""script that starts a Flask web application:"""

from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def Hello():
    """returns a string(hello)"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns a string(HBNB)"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """returns a C followed by the value of a variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """returns Python followed by the value of a variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """returns "nis a number only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
