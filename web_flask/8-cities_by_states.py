#!/usr/bin/python3
"""
This Python script starts a
Flask application
"""


from flask import Flask as f, render_template as r
from models import storage
app = f(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    This cities_by_states route displays the states and cities
    listed in alphabetical order
    """
    states = storage.all("State").values()
    return r('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """This method closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
