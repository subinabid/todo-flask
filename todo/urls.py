from flask import Blueprint, render_template, session
from todo.models import User

app = Blueprint("urls", __name__)


# Index
@app.route("/")
def index():
    if session.get("user") is not None:
        user = User.query.filter_by(username=session["user"]).first()
        tasks = user.tasks.filter_by(complete=False)
        return render_template("index.html", tasks=tasks)

    return render_template("index.html")
