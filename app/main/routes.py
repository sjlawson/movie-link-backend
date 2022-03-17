from flask import request, jsonify
from app.search import lens_search
from app.main import bp


@bp.route("/")
@bp.route("/index")
def index():
    return "Not found", 404


@bp.route("/test")
@bp.route('/healthcheck')
def test():
    return "OK"


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

    Strategy:
    Use "Bag of words" technique to sort terms into text and numeric
    Leave User_id and timestamp (sort fields) out of the search algo
      - Integers will be searched out of movie_id, imdb_id, and tmdb_id
      - if a float is found, only have to search rating
      - word input will be searched from title, genre, and tag
    """
    args = request.args
    result = lens_search(args)  # [{"sample": {"title": "The Thing", "rating": "4.1"}}, ]
    return jsonify({'search_query': args, 'result': result})
