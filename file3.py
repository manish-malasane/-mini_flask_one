"""
How to run flask application as a script instead of using long CLI command
  Write entry point clause :->
    -> We have a function called run in Flask class which takes host, port number, debug, ....
        it can also work if we did not mention all the above things as arguments

- MarkupSafe :-> used for URL`s
- Jinja2 :-> used for templating
- Flask :- flask is flask
- Werkzeug :- In this flask core functionality is written
- click :-> used for command line application
"""

from flask import Flask

# Flask is a class we used to instantiate an application
app = Flask(__name__)


# route decorater allows us to bind a function with certain `relative URL path`
@app.route("/hello")
def hello():
    return "Hello, How are you?"


# Write entrypoint clause
if __name__ == "__main__":
    app.run(host="localhost",
            port=8080,
            debug=True)

    # app.run(host="127.0.0.1",
    #         port=8080,
    #         debug=True)
