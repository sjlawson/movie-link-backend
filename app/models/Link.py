from app.models.Movie import Movie
from sqlalchemy import orm, Column, Integer, ForeignKey, String
from app import db
import json


class Link(db.Model):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.movie_id), nullable=False)
    movie = orm.relationship(Movie, backref=orm.backref('links', uselist=True))
    imdb_id = Column(String(20))
    tmdb_id = Column(String(20))

    def __repr__(self):
        return json.dumps({"imdb": self.imdb_id, "tmdb": self.tmdb_id})
