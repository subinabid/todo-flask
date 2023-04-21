import os
from flask import Flask
from todo.models import db
from todo import auth, urls


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

    # Register Blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(urls.bp)

    return app
