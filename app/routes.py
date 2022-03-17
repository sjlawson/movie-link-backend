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
    search_query = request.json
    result = [{"sample": {"title": "The Thing", "rating": "4.1"}}, ]
    return jsonify({'search_query': search_query, 'result': result})
