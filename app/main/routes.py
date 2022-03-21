from flask import request, jsonify

from app.models.dependencies import model_dependency_injection
from app.main.inputs import movie_search
from app.main.parse import clean
from app.search import lens_search
from app.main import bp


@bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'OK'}), 200


@bp.route('/s', methods=['GET'])
def search():
    """
    GET is generally preferred for search so users can bookmark the result page

    text search fields:
        Movie.title,genres
        Tag.tag
    numeric search fields:
        Movie.movie_id
        Link.imdb_id,tmdb_id
    aggregate field
        Rating.rating
    separate filter/sort field:
        user_id
        timestamp

    """
    # run the input through a custom API reverse serializer
    movie_search_args = clean(request.args, movie_search)
    result = lens_search(movie_search_args.data, *model_dependency_injection())
    return jsonify({'search_query': request.args, 'result': [movie.serialize for movie in result]})
