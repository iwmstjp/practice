from flask import Flask
from flask import render_template, request
import requests

url = "https://api.npoint.io/7f61d8933e17ba5e2424"
# response = requests.get(url)
# print(response.json())
# posts = response.json()
posts=[
    {
        "id":1,
        "title":"The life of Cacuts",
        "subtitle":"Who knows",
        "body":"A cactus (pl.: cacti, cactuses, or less commonly, cactus)[3] is a member of the plant family Cactaceae (/kæˈkteɪsiaɪ, -siːiː/),\
        [a] a family comprising about 127 genera with some 1,750 known species of the order Caryophyllales.[4] The word cactus derives, through Latin, \
        from the Ancient Greek word κάκτος (káktos), a name originally used by Theophrastus for a spiny plant whose identity is now not certain "
    },
    {
        "id":2,
        "title":"The life of Cats",
        "subtitle":"strage of life",
        "body":"The cat (Felis catus), commonly referred to as the domestic cat or house cat, is the only domesticated species in the family Felidae.\
        Recent advances in archaeology and genetics have shown that the domestication of the cat occurred in the Near East around 7500 BC. It is commonly\
        kept as a house pet and farm cat, but also ranges freely as a feral cat avoiding human contact. It is valued by humans for companionship and its ability to kill vermin."
    }
]
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['get','post'])
def contact():
    flag = False
    if request.method == 'POST':
        print(request.form.get('name'))
        flag = True
        return render_template("contact.html", flag=flag)
    else:
        return render_template("contact.html", flag=flag)


@app.route("/post/<int:index>")
def post(index):
    request_post = None
    for post in posts:
        if post["id"] == index:
            request_post = post
    return render_template("post.html", post=request_post)

if __name__ == "__main__":
    app.run(debug=True)