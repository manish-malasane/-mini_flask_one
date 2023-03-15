"""
REST API needs to be stateless
"""

from datetime import datetime
from flask import Flask


app = Flask(__name__)


@app.route("/welcome")
def welcome():
    return "Welcome to the page"


@app.route("/date")
def date():
    return f"This application is serving you at \t {str(datetime.now())}"


counter = 0  # for counting how much time user is visiting the page we need global `counter` variable


@app.route("/view_count")
def refresh_count():
    global counter
    counter += 1
    return f"This page is visited {counter} times"


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0", debug=True)
