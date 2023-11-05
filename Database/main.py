from flask import Flask, render_template, request
from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

class MyForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    rating = StringField('rating', validators=[DataRequired()])

app = Flask(__name__)

all_books = []
csrf = CSRFProtect(app)
SECRET_KEY = "secret_key"
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['get', 'post'])
def add():
    form = MyForm()
    if request.method == 'POST':
        book = { 'title':request.form.get('title'), 'author':request.form.get('author'), 'rating':request.form.get('rating')}
        all_books.append(book)
        print(all_books)
        return render_template('index.html', books=all_books)
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

