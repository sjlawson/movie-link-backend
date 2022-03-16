from app import create_app, db
import pytest

from app.helpers import import_movie_data
from config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig())
    return app


@pytest.fixture
def test_database():
    db.create_all()
    import_movie_data()
    yield db
    db.drop_all()
