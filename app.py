from flask import flask

app = flask(__name__)

@app.route("/")
def hello():
    return "Welcome PN - This is a hello world application "

