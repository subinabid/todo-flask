from flask import Blueprint, request, render_template, session, flash, redirect, url_for
from todo.models import db, User, Task
from datetime import date
from datetime import datetime

app = Blueprint("task", __name__, url_prefix="/tasks")


# Add a task
# Needs login_required decorator
@app.route("/add", methods=["POST"])
def add():
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
        username = db.one_or_404(db.select(User).filter_by(username=session["user"]))
        t = Task(user=username, task=task_text, target_date=task_date)
        db.session.add(t)
        db.session.commit()

        flash(f"Task - {task_text} added")

    else:
        flash(error)

    return redirect("/")


# Mark a task as closed
@app.route("<int:id>", methods=["POST"])
def update(id):
    t = db.get_or_404(Task, id)
    t.complete = request.json["completed"]
    db.session.commit()

    return redirect("/")


# Delete a task
@app.route("<int:id>", methods=["DELETE"])
def delete(id):
    t = db.get_or_404(Task, id)
    db.session.delete(t)
    db.session.commit()

    return redirect("/")


# Update task text
@app.route("<int:id>/changetask", methods=["POST"])
def update_text(id):
    t = db.get_or_404(Task, id)
    t.task = request.json["task"]
    db.session.commit()

    return redirect("/")


# Update Task date
@app.route("<int:id>/changedate", methods=["POST"])
def update_date(id):
    t = db.get_or_404(Task, id)
    t.target_date = datetime.strptime(request.json["date"], "%Y-%m-%d")
    db.session.commit()

    return redirect("/")


# Archive a task
# Why am I not reusing the above API?
@app.route("<int:id>/archive")
def archive(id):
    t = db.get_or_404(Task, id)
    t.archive = True
    db.session.commit()

    return redirect("/")


# Unrchive a task
@app.route("<int:id>/unarchive")
def unarchive(id):
    t = db.get_or_404(Task, id)
    t.archive = False
    db.session.commit()

    return redirect(url_for("task.archives"))


# List of completed tasks
@app.route("/archives")
def archives():
    if session.get("user") is not None:
        user = User.query.filter_by(username=session["user"]).first()
        tasks = user.tasks.filter_by(archive=True)
        return render_template("archive.html", tasks=tasks)

    flash("Unknown Error")
    return redirect("/")
