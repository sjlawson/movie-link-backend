from app import create_app
import pytest
from config import TestConfig
from tests.db_setup import seed_test_data


@pytest.fixture(scope="session")
def test_app():
    app = create_app(TestConfig())
    with app.app_context():
        db = seed_test_data()
        yield app
        db.drop_all()


