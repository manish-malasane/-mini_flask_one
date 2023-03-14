"""
By default, whatever path parameter we passed is converted into string
We can do type hinting like 2nd application in this module
NOTE:
    Visit this :-> https://flask.palletsprojects.com/en/2.2.x/quickstart/#variable-rules
"""

from flask import Flask

# Flask is a class we used instantiate an application
app = Flask(__name__)


##############################################################################
#                How to create path parameter in flask?                      #
##############################################################################

# route decorater allows us to bind a function with certain `relative URL path`
@app.route("/path/<username>")  # when we browse this url in browser we have to pass relative path as mentioned
def show_user_profile(username):  # here we have to fetch user data based on whatever parameter we passed
    # show user profile based on username
    # logic goes here
    return f"{username} your profile has been created"


##############################################################################
#            How to create path parameter in flask with data types?          #
##############################################################################

# route decorater allows us to bind function with certain `relative URL path`
@app.route("/story/<int:story_number>")
def story_teller(story_number):  # here we are fetching story data based on whatever story number we are passing in url
    # for showing story data logic goes here
    return f"[ INFO ] DETAILS of Story Number:-> {story_number}"


