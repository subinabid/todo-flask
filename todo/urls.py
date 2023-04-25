from flask import Blueprint, render_template, session
from todo.models import User

bp = Blueprint("urls", __name__)


# Index
@bp.route("/")
def index():
    if session.get("user") is not None:
        user = User.query.filter_by(username=session["user"]).first()
        tasks = user.tasks
        return render_template("index.html", tasks=tasks)

    return render_template("index.html")
