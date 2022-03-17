from app import db
import pandas as pd

from app.models.Link import Link
from app.models.Movie import Movie
from app.models.Rating import Rating
from app.models.Tag import Tag


def import_movie_data():
    names = ["movie_id", "title", "genres"]
    df = pd.read_csv("./data_import/movies.csv", names=names, skiprows=1)
    df.to_sql(
        con=db.engine, index_label="id", name=Movie.__tablename__, if_exists="replace"
    )


def import_link_data():
    names = ['movie_id', 'imdb_id', 'tmdb_id']
    df = pd.read_csv("./data_import/links.csv", names=names, skiprows=1)
    df.to_sql(
        con=db.engine, index_label="id", name=Link.__tablename__, if_exists="replace"
    )


def import_rating_data():
    names = ['user_id', 'movie_id', 'rating', 'timestamp']
    df = pd.read_csv("./data_import/ratings.csv", names=names, skiprows=1)
    df.to_sql(
        con=db.engine, index_label="id", name=Rating.__tablename__, if_exists="replace"
    )


def import_tag_data():
    names = ['user_id', 'movie_id', 'tag', 'timestamp']
    df = pd.read_csv("./data_import/tags.csv", names=names, skiprows=1)
    df.to_sql(
        con=db.engine, index_label="id", name=Tag.__tablename__, if_exists="replace"
    )
