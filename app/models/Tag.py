from app.models.Movie import Movie
from sqlalchemy import orm, Column, String, Integer, ForeignKey, func
from app import db


class Tag(db.Model):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    movie_id = Column(Integer, ForeignKey(Movie.movie_id), nullable=False)
    movie = orm.relationship(Movie, backref=orm.backref("tags", uselist=True))
    tag = Column(String(150))
    timestamp = Column(
        Integer, default=func.now(), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return self.tag
