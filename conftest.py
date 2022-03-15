from app import create_app
import pytest


@pytest.fixture
def app():
    app = create_app()
    return app


# class UserModelCase(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app(TestConfig)
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()
#
#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()
