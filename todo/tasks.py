from flask import Blueprint, request, render_template, session, flash
from todo.models import db, User, Task
from datetime import date
from datetime import datetime

bp = Blueprint("task", __name__, url_prefix="/task")


# Add a task
# Needs login_required decorator
@bp.route("/add", methods=("GET", "POST"))
def task_add():
    if request.method == "POST":
        error = None
        task_text = request.form["task"]
        input_date = request.form["target_date"]

        if input_date == "":
            task_date = date.today()
        else:
            task_date = datetime.strptime(input_date, "%Y-%m-%d")

        if not task_text:
            error = "Task description is missing"

        if error is None:
            username = db.one_or_404(
                db.select(User).filter_by(username=session["user"])
            )
            t = Task(user=username, task=task_text, target_date=task_date)
            db.session.add(t)
            db.session.commit()

            flash(f"Task - {task_text} added")

        else:
            flash(error)

    return render_template("tasks/add.html")
