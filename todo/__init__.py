import os
from flask import Flask
from flask_migrate import Migrate
from todo.models import db
from todo import auth, urls, tasks


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///todo.db",
    )

    # Create the instance_path folder
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Use the Database
    db.init_app(app)

    # Enable database migrations
    migrate = Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(auth.app)
    app.register_blueprint(urls.app)
    app.register_blueprint(tasks.app)

    return app
