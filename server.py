from flask import Flask
from flask import render_template
import requests

url = "https://api.npoint.io/7f61d8933e17ba5e2424"
response = requests.get(url)
# print(response.json())
posts = response.json()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def post(index):
    request_post = None
    for post in posts:
        if post["id"] == index:
            request_post = post
    return render_template("post.html", post=request_post)

if __name__ == "__main__":
    app.run(debug=True)