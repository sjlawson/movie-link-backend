from app.models.Movie import Movie


def test_app_setup(app, test_database):
    """
    Make sure there is an app context and seed data has been imported from given csv files
    :param app:
    :param test_database:
    :return:
    """
    db = test_database
    movie = db.session.query(Movie).first()
    assert str(movie) == "Toy Story (1995)"
