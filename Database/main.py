from flask import Flask, render_template, request, redirect,url_for
from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

class MyForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    rating = StringField('rating', validators=[DataRequired()])

class ratingForm(FlaskForm):
    rating = StringField('rating', validators=[DataRequired()])

db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer)

csrf = CSRFProtect(app)
SECRET_KEY = "secret_key"
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book)).scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['get', 'post'])
def add():
    form = MyForm()
    if request.method == 'POST':
        book = Book(title=request.form.get('title'),
                author=request.form.get('author'),
                rating=request.form.get('rating'))
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route("/edit/<int:book_id>", methods=['get', 'post'])
def edit(book_id):
    form = ratingForm()
    book = db.get_or_404(Book, book_id)
    if request.method == 'POST':
        print(request.form.get('rating'))
        book.rating = request.form.get('rating')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", book=book, form=form)

@app.route("/delete", methods=['get', 'post'])
def delete():
    book = db.get_or_404(Book, request.args.get('book_id'))
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

