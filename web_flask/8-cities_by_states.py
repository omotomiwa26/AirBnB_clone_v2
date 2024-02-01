#!/usr/bin/python3
"""
This Python script starts a
Flask application
"""


from flask import Flask as f, render_template as r
from models import storage
app = f(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    This states route displays the states and cities listed
    in alphabetical order
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return r('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """This method closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
