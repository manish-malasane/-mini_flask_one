# how to capture query parameters so, we have to import ```request``` from flask
# ```request``` is a global object it is present in all the flask applications


from flask import Flask, request

# we use request for capturing the query params from application and, it is a global variable
# flask is a class we used to instantiate an application
app = Flask(__name__)

##############################################################################
#                How to create path parameter in flask?                     #
##############################################################################


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"<h1>{subpath}</h1>"


##############################################################################
#                How to access query parameter in flask?                     #
##############################################################################

# route decorater allows us to bind a function with certain `relative URL path`
@app.route("/about")
def institute():
    institute_name = request.args.get("institute")
    return f"<p>{institute_name}</p>"


if __name__ == "__main__":
    app.run(debug=True)
