from app.models.Link import Link
from app.models.Movie import Movie, Rating
from app.models.Tag import Tag


def test_app_setup(test_app):
    """
    Make sure there is an app context and seed data has been imported from given csv files
    :param app:
    :param test_database:
    :return:
    """
    with test_app.app_context():
        movie = Movie.query.first()
        assert str(movie) == "Toy Story (1995)"

        link = Link.query.first()
        assert str(link) == '{"imdb": "114709", "tmdb": "862.0"}'

        rating = Rating.query.first()
        assert str(rating) == "4.0"

        tag = Tag.query.first()
        assert str(tag) == "funny"
