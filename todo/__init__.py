import os
from flask import Flask, render_template
from todo.models import User


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        # DATABASE=os.path.join(app.instance_path, "todo.sqlite"),
        SQLALCHEMY_DATABASE_URI="sqlite:///todo.db",
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from todo.models import db

    db.init_app(app)

    @app.route("/")
    def index():
        return "ToDo-Flask"

    @app.route("/db")
    def db():
        users = User.query.all()
        return render_template("db.html", users=users)

    return app
