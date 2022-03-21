from app import db
import pandas as pd
from flask import current_app
from app.models.Link import Link
from app.models.Movie import Movie, Rating
from app.models.Tag import Tag


def import_movie_data():
    if db.session.query(Movie).first() is not None:
        print("Movie data already loaded")
        return

    names = ["movie_id", "title", "genres"]
    # Pandas provides a fast method of importing large data sets
    df = pd.read_csv("./data_import/movies.csv", names=names, skiprows=1)
    df["rating_avg"] = 0
    df.to_sql(con=db.engine, index=False, name=Movie.__tablename__, if_exists="append")


def import_link_data():
    if db.session.query(Link).first() is not None:
        print("Link data already loaded")
        return

    names = ["movie_id", "imdb_id", "tmdb_id"]
    df = pd.read_csv("./data_import/links.csv", names=names, skiprows=1)
    df.to_sql(
        con=db.engine, index_label="id", name=Link.__tablename__, if_exists="append"
    )


def import_rating_data():
    """
    There is a trade-off here. The import will take a long time, but will speed up the front end by maintaining
    an aggregated column for average ratings.
    To pre-populate the aggregated rating data, just touch one rating for each movie in the db
    this is basically a no-op that tricks slqalchemy into updating the aggregated rating_avg field
    :return:
    """
    if db.session.query(Rating).first() is not None:
        print("Rating data already loaded")
        return

    names = ["user_id", "movie_id", "rating", "timestamp"]
    df = pd.read_csv("./data_import/ratings.csv", names=names, skiprows=1)
    df.to_sql(
        con=db.engine, index_label="id", name=Rating.__tablename__, if_exists="append"
    )

    if not current_app.config["TESTING"]:
        # skip the big update for testing
        ratings = Rating.query.group_by(Rating.movie_id).all()
        db.session.add_all(ratings)
    rating = Rating.query.first()
    # This line wants to say, "Look, I have one job on this lousy ship. It's stupid, but I'm going to do it, okay?"
    rating.timestamp += 0
    db.session.add(rating)
    db.session.commit()


def import_tag_data():
    if db.session.query(Tag).first() is not None:
        print("Tag data already loaded")
        return

    names = ["user_id", "movie_id", "tag", "timestamp"]
    df = pd.read_csv("./data_import/tags.csv", names=names, skiprows=1)
    df.to_sql(
        con=db.engine, index_label="id", name=Tag.__tablename__, if_exists="append"
    )
