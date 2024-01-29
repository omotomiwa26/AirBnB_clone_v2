#!/usr/bin/python3
"""
This Python script starts a
Flask application
"""


from flask import Flask as f
app = f(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    This flask home route returns Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This flask hbnb route returns Hello HBNB!
    """
    return 'HBNB!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
