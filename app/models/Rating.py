from app import db
from app.models.Movie import Movie
from sqlalchemy.orm import backref


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.movie_id), nullable=False)
    movie = db.relationship(Movie, backref=backref('ratings', uselist=False))
    rating = db.Column(db.Numeric(2, 1), nullable=True)
    timestamp = db.Column(db.Integer)

    def __repr__(self):
        return str(self.rating)

