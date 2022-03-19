from sqlalchemy_utils import escape_like


def lens_search(params):
    """
    chances are if someone enters a full title, they aren't concerned about genres
    :param params:
    :return:
    """
    title_result = []
    if params['title'] and not params['genres'] and not params['tags']:
        title_result = search_title(params['title'])

    return [*title_result]


def search_title(query):
    """
    First search for title match
    If no exact, eliminate stop words and search bag-of-words
    :return:
    """
    # Had to move this import from module scope to function scope to avoid circular import
    # I think this might also be fixed by refactoring the db seed function in cli
    from app.models.Movie import Movie
    query = escape_like(query)
    return Movie.query.filter(Movie.title.like(f'%{query}%')).all()


def search_numeric():
    pass
