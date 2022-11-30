from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

MOVIE_ENDPOINT = 'https://api.themoviedb.org/3/search/movie'
MOVIE_ADD_ENDPOINT = 'https://api.themoviedb.org/3/movie'
API_KEY = '9d35ea09da55e5ead11b65c1bca8397d'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


with app.app_context():
    class Movie(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), unique=True, nullable=False)
        year = db.Column(db.Integer, nullable=False)
        description = db.Column(db.String(200), nullable=False)
        rating = db.Column(db.Float)
        ranking = db.Column(db.Integer)
        review = db.Column(db.String(500))
        img_url = db.Column(db.String(300), nullable=False)

        # def __repr__(self):
        #     return f"<Movie {self.title}>"

    db.create_all()

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

class RateAndReviewForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/add', methods=["GET", "POST"])
def add():
    form = MovieForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            movie_title = request.form.get('title')
            response = requests.get(MOVIE_ENDPOINT, params={"api_key": API_KEY, "query": movie_title})
            data = response.json()['results']
            return render_template("select.html", data=data)
    return render_template('add.html', form=form)


@app.route('/select')
def select():
    movie_id = request.args.get('id')
    print(movie_id)
    if movie_id:
        MOVIE_URL = f'{MOVIE_ADD_ENDPOINT}/{movie_id}'
        # MOVIE_URL = f'{MOVIE_ENDPOINT}/{movie_id}?api_key={API_KEY}'
        response = requests.get(MOVIE_URL, params={"api_key": API_KEY})
        data = response.json()
        print(data)
        new_movie = Movie(
            title = data['original_title'],
            year = data['release_date'].split("-")[0],
            description = data['overview'],
            img_url = data['poster_path']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit'))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    movie_id = request.args.get('id')
    form = RateAndReviewForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            rate = request.form['rating']
            review = request.form['review']
            movie = Movie.query.filter_by(id=movie_id).first()
            movie.rating = rate
            movie.review = review
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)