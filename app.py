from flask import Flask, flash, redirect, render_template, request, session, abort
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/makePrediction", methods = ['GET'])
def makePrediction():
    return str(datetime.datetime.now().year)

if __name__ == "__main__":
    app.run()