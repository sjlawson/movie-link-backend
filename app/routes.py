from flask import Blueprint, request, jsonify

bp = Blueprint("main", __name__)


@bp.route("/")
@bp.route("/index")
def index():
    return "Not found", 404


@bp.route("/test")
@bp.route('/healthcheck')
def test():
    return "OK"


@bp.route('/s', methods=['POST'])
def search():
    """
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
    search_query = request.json
    result = [{"sample": {"title": "The Thing", "rating": "4.1"}}, ]
    return jsonify({'search_query': search_query, 'result': result})


