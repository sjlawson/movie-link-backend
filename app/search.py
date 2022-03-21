from sqlalchemy import or_


def lens_search(params, db, Movie, Tag, *args):
    """
    chances are if someone enters a full title, they aren't concerned about genres
    :param params:
    :return:
    """
    query = db.session.query(Movie)

    if not params:
        return query.order_by(Movie.title).all()

    if params.get("title") and len(params) == 1:
        return query.filter(Movie.title.like(f'%{params["title"]}%')).all()

    return multi_filter_search(params, query, Movie, Tag)


def multi_filter_search(params, query, Movie, Tag):
    if params.get("title"):
        query = query.filter(Movie.title.like(f'%{params["title"]}%'))
    if params.get("genres"):
        # I think this should be an 'OR' search...
        genres = [g.strip() for g in params.get("genres").split(",")]
        genre_expressions = [Movie.genres.like(f"%{genre}%") for genre in genres]
        query = query.filter(or_(*genre_expressions))
    if params.get("tags"):
        tags = [t.strip() for t in params.get("tags").split(",")]
        tags_expressions = [Tag.tag.like(f"%{tag}%") for tag in tags]
        query = query.join(Tag).filter(or_(tags_expressions))
    if rating := params.get("rating"):
        try:
            if "-" in rating:
                rating_range = [float(r.strip()) for r in rating.split("-")]
            else:
                # let's make it within 0.1 of the entered value
                rating = float(rating)
                rating_range = [rating - 0.1, rating + 0.1]
            query = query.filter(Movie.rating_avg >= rating_range[0]).filter(
                Movie.rating_avg <= rating_range[1]
            )
        except ValueError:  # if it's not a good input, just leave it out
            pass

    return query.all()
