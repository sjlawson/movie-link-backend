from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from app.main import routes

db = SQLAlchemy()
# migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(routes.bp, url_prefix='/api/v1')
    db.init_app(app)
    # migrate.init_app(app, db)

    return app
