from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.mtheod == 'GET':
        return 'Hello, World com GET'
    return "<p> Hello, World com POST</p>"

@app.route("/json")
def json():
    return {
        'message': "Olá Mundo"
    }


with app.test_request_context():
    print(url_for("hello_world"))
    print(url_for("json"))