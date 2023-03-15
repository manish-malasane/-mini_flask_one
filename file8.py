import json
import pydantic.error_wrappers
from flask import Flask, request
from pydantic import BaseModel


class ScoreRequestInput(BaseModel):
    player_name: str
    age: int
    score: int


class ScoreResponseOutput(BaseModel):
    player_name: str
    age: int
    score: int
    msg: str


app = Flask(__name__)


class MyDB:
    foo = []


@app.get("/get_data")
def get_data():
    return f"Available Data :-> {MyDB.foo}"


@app.post("/post_data")
def post_data():
    body = request.data
    data = json.loads(body)

    try:
        data = ScoreRequestInput(**data)
    except pydantic.ValidationError:
        return "Invalid Input"

    msg = "Better Luck, \n Next time.."
    if data.score >= 100:
        msg = f"Congratulations, For Scoring {data.score}"

    response = {
        "player_name": "Mr." + data.player_name,
        "age": data.age,
        "score": data.score,
        "msg": msg
                }
    try:
        ScoreResponseOutput(**response)
        return response
    except pydantic.ValidationError:
        return "Invalid Output"
