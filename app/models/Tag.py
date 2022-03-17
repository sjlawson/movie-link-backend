from app import db
from app.models.Movie import Movie
from sqlalchemy.orm import backref


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.movie_id), nullable=False)
    movie = db.relationship(Movie, backref=backref('tags', uselist=False))
    tag = db.Column(db.String(150))
    timestamp = db.Column(db.Integer)

    def __repr__(self):
        return self.tag
