from app import create_app, db
import pytest

from app.helpers import import_movie_data, import_link_data, import_rating_data, import_tag_data
from config import TestConfig


@pytest.fixture(scope="session")
def app():
    app = create_app(TestConfig())
    return app


@pytest.fixture(scope="package")
def test_database(app):
    with app.app_context():
        db.create_all()
        import_movie_data()
        import_link_data()
        import_rating_data()
        import_tag_data()
        yield db
        db.drop_all()
