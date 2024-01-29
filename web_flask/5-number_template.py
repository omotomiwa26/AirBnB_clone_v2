#!/usr/bin/python3
"""
This Python script starts a
Flask application
"""

import re
from flask import Flask as f, render_template as r
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
    This flask hbnb route returns HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This flask c_text route returns 'C'
    followed by the value of text variable
    """
    return 'C ' + re.sub('_', ' ', text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    This flask python_text route returns 'Python'
    followed by the value of text variable
    """
    return 'Python ' + re.sub('_', ' ', text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n) -> int:
    """
    This flask number route returns 'n is a number'
    only if n is an integer
    """
    return F'{n:d} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n) -> int:
    """
    This flask number_template route displays an HTML page
    only if n is an integer
    """
    return r('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
