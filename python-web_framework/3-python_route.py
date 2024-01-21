#!/usr/bin/python3
'''Importing Flask form flask'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = escape(text).replace("_", " ")
    return f'C {text}'

@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = escape(text).replace("_", " ")
    return 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

# /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
# The default value of text is “is cool”

