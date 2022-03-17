from app import db
from app.helpers import import_movie_data, import_link_data, import_rating_data, import_tag_data


def seed_test_data():
    db.create_all()
    import_movie_data()
    import_link_data()
    import_rating_data()
    import_tag_data()
    return db
