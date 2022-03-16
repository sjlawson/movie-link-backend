from flask import Blueprint

bp = Blueprint("main", __name__)


@bp.route("/")
@bp.route("/index")
def index():
    return "Hello, World!"


@bp.route("/test")
def test():
    return "OK"
    # with db.cursor() as cur:
    #     cur.execute("SELECT col FROM test;")
    #     (result,) = cur.fetchone()
    #     return flask.jsonify(dict(result=result, backend="python"))
