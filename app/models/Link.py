from app import db
from app.models.Movie import Movie
from sqlalchemy.orm import backref


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.movie_id), nullable=False)
    movie = db.relationship(Movie, backref=backref('links', uselist=False))
    imdb_id = db.Column(db.Integer)
    tmdb_id = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.movie.title} links'
