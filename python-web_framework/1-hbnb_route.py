#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/number/<int:num>')
def show_number(num):
    return render_template('5-number.html', number=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
