from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)


with app.app_context():
    db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
# )

# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars().all()

    for i, movie in enumerate(all_movies):
        movie.ranking = i + 1

    return render_template("index.html", movies=all_movies)


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/update", methods=["GET", "POST"])
def update():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    form = RateMovieForm()

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data

        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": API_KEY,
                "query": movie_title,
            },
        )

        data = response.json()
        movies = data["results"]

        return render_template("select.html", movies=movies)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_id = request.args.get("id")

    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}",
        params={
            "api_key": API_KEY,
        },
    )

    data = response.json()
    movie = Movie(
        title=data["title"],
        year=int(data["release_date"][:4]),
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        rating=0,
        ranking=10,
        review="",
    )

    db.session.add(movie)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
