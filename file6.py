from flask import Flask, render_template
"""
              In terms of web frameworks

                      ```MVC```

M :- Model         (For database related functionality)
V :- View          (Whatever we are seeing on the user interface OR frontend)
C :- Controller    (Whatever logic we write behind of that view OR backend) (business logic)
"""

"""
            In terms of web frameworks in python
            
                      ```MVC``` is ```MVT```

M :- Model         (For database related functionality)
V :- View          (Whatever logic we write behind of that view OR backend) (business logic)
T :- Template      (Whatever we are seeing on the user interface OR frontend)
"""

"""
Whatever html we passed through our file9.py application we called it as a rendering and for this we have to import 
`render_template()` function from file9.py.
- render_template mandatory takes one argument as a template_name(html file from template folder) 
- When we use render_template function it looks for template directory named as templates itself
"""
"______________________________________________________________________________________________________________________"
"""
- In order to render template in file9.py, we need to create folder named `templates`
- The folder can contain all the html files required in the project
"""

# Flask is a class we used to instantiate an application
app = Flask(__name__)


# route decorater allows us to bind a function with certain (relative URL path)
@app.route("/hello")  # URL Binding
def basic():
    return render_template("basic.html")  # from here we render the template on browser
