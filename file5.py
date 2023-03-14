"""
in global ```request``` variable there is a attribute called data and json to capture the json data
- by doing request.data. we get data as a byte string
- by doing request.json we get data as a byte string

"""
import json
from flask import Flask, request

# flask is a class we used to instantiate an application
app = Flask(__name__)


class MyDB:
    """
    Class that is runtime database
    Note:
        This database is going to persist data as long as application is in running state
    """
    foo = []


# route decorater allows us to bind a function with certain `relative URL path`.
@app.get("/get_data")
def get_data():
    """
    HTTP GET request from postman/browser
    Returns:

    """
    return f"Available data:-> {MyDB.foo}"


@app.post("/post_data")
def post_data():
    """
    HTTP POST request with JSON payload
    Returns:

    """
    body = request.data  # this data is in byte string format so, we have to serialize that data
    data = json.loads(body)

    for val in data.values():
        MyDB.foo.append(val)

    return f"Latest data :-> {MyDB.foo}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
