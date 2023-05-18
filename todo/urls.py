from flask import Blueprint, redirect, render_template, session, url_for
from todo import auth
from todo.models import User

app = Blueprint("urls", __name__)


# Index
@app.route("/")
def index():
    if session.get("user") is not None:
        user = User.query.filter_by(username=session["user"]).first()
        tasks = user.tasks.filter_by(archive=False)
        return render_template("index.html", tasks=tasks)
    else:
        return redirect(url_for('auth.login'))

