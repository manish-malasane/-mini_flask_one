from flask import Flask

# Flask is a class we used to instantiate an application
app = Flask(__name__)  # Takes one argument as current module name


# First HTTP GET request
# route decorater allows us to bind function to certain `relative URL path`
@app.route("/")
def first_app():
    print(f"{__name__} running")
    return "<p>Hello, World!</p>"


# Second HTTP GET request
@app.route("/hello")  # These are endpoints
def greeting():
    import requests
    data = requests.get("https://swapi.dev/api/films/1")
    # store data in database logic goes here
    return f"""{data.json()} 
    <h1>Data has been stored in database</h1>"""
