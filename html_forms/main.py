from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['post'])
def receive_data():
    userdata = request.form
    return render_template("login.html", userdata=userdata)


if __name__ == "__main__":
    app.run(debug=True)