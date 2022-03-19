from app import db


class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    genres = db.Column(db.String(400))

    def __repr__(self):
        return self.title

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
            'genres': self.genres,
        }
