from flask import Blueprint, request, render_template, session, flash, redirect
from todo.models import db, User, Task
from datetime import date
from datetime import datetime

app = Blueprint("task", __name__, url_prefix="/tasks")


# Add a task
# Needs login_required decorator
@app.route("/add", methods=("GET", "POST"))
def add():
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


# Mark a task as closed
@app.route("<int:id>", methods=["POST"])
def update(id):
    t = db.get_or_404(Task, id)
    t.complete = request.json["completed"]
    db.session.commit()

    return redirect("/")


# List of completed tasks
@app.route("/completed")
def completed():
    if session.get("user") is not None:
        user = User.query.filter_by(username=session["user"]).first()
        tasks = user.tasks.filter_by(complete=True)
        return render_template("completed.html", tasks=tasks)

    flash("Unknown Error")
    return redirect("/")
