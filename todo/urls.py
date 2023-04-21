from flask import Blueprint, render_template
from todo.models import User

bp = Blueprint("urls", __name__)


# Index
@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/db")
def db():
    users = User.query.all()
    return render_template("db.html", users=users)
