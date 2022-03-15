from app import db


class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    genres = db.Column(db.String(400))

