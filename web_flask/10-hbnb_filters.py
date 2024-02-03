#!/usr/bin/python3
"""
This Python script starts a
Flask application
"""


from flask import Flask as f, render_template as r
from models import storage
app = f(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    This filter route displays a HTML page like 6-index.htmlfrom static
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return r('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    This method closes the storage on teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
