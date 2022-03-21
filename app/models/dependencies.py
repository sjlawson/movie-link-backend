

def model_dependency_injection():
    """
    A work-around for circular imports that seem to occur because of the model imports in the cli seed function
    :return:
    """
    from app import db
    from app.models.Movie import Movie
    from app.models.Tag import Tag
    from app.models.Link import Link
    from app.models.Movie import Rating
    return db, Movie, Tag, Link, Rating
