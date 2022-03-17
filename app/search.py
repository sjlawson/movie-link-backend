from sqlalchemy_utils import escape_like
from flask import current_app
# from current_app.models.Movie import Movie


def lens_search(params):
    result = [search_title(params['title'])]
    return result


def search_title(query):
    """
    First search for exact title match
    If no exact, eliminate stop words and search bag-of-words
    :return:
    """
    # Movie = current_app.extensions.models.Movie
    query = escape_like(query)
    exact = '' #  Movie.query.filter(Movie.title.like(f'%{query}%')).all()
    return exact


def search_numeric():
    pass
