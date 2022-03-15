import os
import click


def register(app):
    @app.cli.group("movielens")
    def movielens():
        """ Dataset initialization commands """

    @movielens.command()
    def load_movielens():
        print("Loding movielens data")
