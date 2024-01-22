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
    return f'C {text}'(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

