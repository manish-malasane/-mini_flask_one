"""
for rendering the variable from html by jinja we have to use double curly braces outside the variable name
                - {{foo}} # example :- `foo` is a variable name
"""
from flask import Flask, render_template

# Flask is a class we used to instantiate an application
app = Flask(__name__)


vegetables = ["Okra", "Peas", "Cauliflower", "Carrot", "Potato"]


# route decorater allows us to bind a function with certain `relative URL path`.
@app.route("/vege")  # 1st bind URL
@app.route("/vege/<vege_name>")  # 2nd bind URL
def veg_(vege_name=None):
    return render_template(
        "dynamic.html",
        vege_name=vege_name,
        vegetables=vegetables
    )
