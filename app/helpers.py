from app import db
import pandas as pd

from app.models.Movie import Movie


def import_movie_data():
    names = ["movie_id", "title", "genres"]
    df = pd.read_csv("./data_import/movies.csv", names=names, skiprows=1)
    df.to_sql(
        con=db.engine, index_label="id", name=Movie.__tablename__, if_exists="replace"
    )
