#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models.city import City
from models import storage
app = Flask(__name__, static_url_path='/web_flask/static')


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page like 6-index.html from static"""
    states = sorted(storage.all("State").values(),
                    key=lambda state: state.name)
    amenities = sorted(storage.all("Amenity").values(),
                       key=lambda amenity: amenity.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities, cities=cities)


@ app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    """main function"""
    app.run(host='0.0.0.0', port='5000')
