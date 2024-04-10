#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """display a html page with States list sorted
    in alphabetical order"""
    states = sorted(list(storage.all("State").values()),
                    key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@ app.teardown_appcontext
def teardown_db(exeption):
    """closes storage on teardown"""
    storage.close()


if __name__ == "__main__":
    """main function"""
    app.run(host='0.0.0.0', port=5000)
