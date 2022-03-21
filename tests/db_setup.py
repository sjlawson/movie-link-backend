from app import db
from app.helpers import import_movie_data, import_link_data, import_rating_data, import_tag_data
from app.models.Movie import Rating


def seed_test_data():
    db.create_all()
    import_movie_data()
    import_link_data()
    import_rating_data()
    import_tag_data()

    # update one rating to check the aggregation
    pooh = Rating.query.filter(Rating.movie_id == 31193).first()
    pooh.timestamp += 0
    db.session.add(pooh)
    db.session.commit()
    return db
