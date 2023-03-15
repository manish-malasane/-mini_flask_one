from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "GET":
        return "<h1> GET Welcome Data </h1>"

    elif request.method == "POST":
        return "<h1> POST Welcome Data </h1>"
