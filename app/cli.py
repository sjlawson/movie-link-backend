import os
import click

from app.helpers import import_movie_data


def register(app):
    @app.cli.group("movielens")
    def movielens():
        """Dataset initialization commands"""

    @movielens.command()
    def seed_data():
        print("Loding movielens data")
        import_movie_data()
