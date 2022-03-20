from . import parse

movie_search = parse.Object(
    {
        'title': parse.String(),
        'genres': parse.String(),
        'tags': parse.String(),
        'rating': parse.String(),
        'imdb_id': parse.Integer(),
        'tmdb_id': parse.Integer(),
    }
)
