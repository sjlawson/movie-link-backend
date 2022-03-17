from app import create_app, db, cli
from app.models.Link import Link
from app.models.Movie import Movie
from app.models.Rating import Rating
from app.models.Tag import Tag

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Movie": Movie, "Link": Link, "Rating": Rating, "Tag": Tag}
