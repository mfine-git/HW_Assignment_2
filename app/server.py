from flask import Flask
from flask import request, Response
import sys

app = Flask(__name__)
port = sys.argv[1]


@app.route("/")
def home():
    return '<h1>Hello from Flask 9:39!</h2>'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int(port))
