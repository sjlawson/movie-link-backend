import json

from sqlalchemy import orm, func, Column, String, Integer, Numeric, ForeignKey, Float
from sqlalchemy_utils import aggregated
from app import db


class Movie(db.Model):
    __tablename__ = 'movies'
    movie_id = Column(Integer, primary_key=True)
    title = Column(String(1000))
    genres = Column(String(1000))

    def __repr__(self):
        return self.title

    @aggregated('ratings', Column(Float()))
    def rating_avg(self):
        return func.avg(Rating.rating)

    ratings = orm.relationship('Rating', backref='movies')

    @property
    def tag_list(self):
        return [tag.tag for tag in self.tags]

    @property
    def serialize(self):
        """
            Return object data in easily serializable format
            For a production application I might recommend using a full rest library. In this case all we need is a
            simple serializer for the GET request.
        """
        return {
            'movie_id': self.movie_id,
            'title': self.title,
            'tags': self.tag_list,
            'genres': self.genres,
            'rating': self.rating_avg,
            'links': json.loads(str(self.links)),
        }


class Rating(db.Model):
    """
    These two models reference each other, so it's just easier to put them in the same file than make a convoluted
    work-around for the circular import
    """
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    movie_id = Column(Integer, ForeignKey(Movie.movie_id), nullable=False)
    rating = Column(Numeric(2, 1), nullable=True)
    timestamp = Column(Integer, default=func.now(), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return str(self.rating)
