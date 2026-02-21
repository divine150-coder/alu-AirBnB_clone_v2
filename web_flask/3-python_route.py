#!/usr/bin/python3
"""Flask"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """prints Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns "HBNB" """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns the string "C" followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Function called with /python/<text> route """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
