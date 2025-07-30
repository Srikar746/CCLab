from flask import Flask
import os

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello.iam srikar Chandra"

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000)