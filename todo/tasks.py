from flask import (
    Blueprint,
    abort,
    request,
    render_template,
    session,
    flash,
    redirect,
)
from flask import jsonify
from todo.models import db, User, Task
from datetime import date
from datetime import datetime

app = Blueprint("task", __name__, url_prefix="/tasks")


@app.route("/", methods=["GET"])
def index():
    tasks = db.session.execute(db.select(Task).filter_by(archive=False)).scalars()
    dicts = [task.to_dict() for task in tasks]
    return jsonify(dicts)


@app.route("/<int:id>", methods=["GET"])
def get(id):
    t = db.get_or_404(Task, id)
    return jsonify(t.to_dict())


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


# Update a task
@app.route("<int:id>", methods=["POST"])
def update(id):
    t = db.get_or_404(Task, id)
    t.task = request.form.get("task", t.task)
    t.target_date = datetime.strptime(
        request.form.get("date", str(t.target_date)), "%Y-%m-%d"
    )
    t.complete = parse_boolean(request.form.get("completed", t.complete))
    t.archive = parse_boolean(request.form.get("archive", t.archive))

    db.session.commit()
    t = db.get_or_404(Task, id)
    return jsonify(t.to_dict())


# Delete a task
@app.route("<int:id>", methods=["DELETE"])
def delete(id):
    t = db.get_or_404(Task, id)
    db.session.delete(t)
    db.session.commit()

    return redirect("/")


# List of achived tasks
@app.route("/archives")
def archives():
    if session.get("user") is not None:
        user = User.query.filter_by(username=session["user"]).first()
        tasks = user.tasks.filter_by(archive=True)
        return render_template("archive.html", tasks=tasks)

    flash("Unknown Error")
    return redirect("/")


def parse_boolean(val):
    match val:
        case bool():
            return val
        case "true":
            return True
        case "false":
            return False
        case _:
            return abort(400)
