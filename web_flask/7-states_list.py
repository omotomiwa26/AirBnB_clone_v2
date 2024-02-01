#!/usr/bin/python3
"""
This Python script starts a
Flask application
"""


from flask import Flask as f, render_template as r
from models import *
app = f(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    This flask states_list displays an HTML page
    with the states listed in alphabetical order
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return r('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """This method closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
