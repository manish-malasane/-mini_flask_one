from flask import Flask, url_for

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello, World !"


@app.route("/user/<username>")
def user_profile(username):
    return f"{username}\'s profile"


# this we write for test cases (unit test).
with app.test_request_context():
    print(url_for("hello"))
    print(url_for("user_profile", username="Manthan Malasane"))
