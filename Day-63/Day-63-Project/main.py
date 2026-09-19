from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)

db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


# Create table
with app.app_context():
    db.create_all()


# HOME
@app.route("/")
def home():
    all_books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("index.html", books=all_books)


# ADD
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book = db.get_or_404(Book, id)

    if request.method == "POST":
        new_rating = request.form["rating"]
        book.rating = float(new_rating)

        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit-rating.html", book=book)


@app.route("/delete/<int:id>")
def delete(id):
    book = db.get_or_404(Book, id)

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
