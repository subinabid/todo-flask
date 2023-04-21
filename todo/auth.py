from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from todo.models import db, User

bp = Blueprint("auth", __name__, url_prefix="/auth")


# Register a user
@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is missing"

        if error is None:
            try:
                u = User(username=username, password=generate_password_hash(password))
                db.session.add(u)
                db.session.commit()

            except:
                error = "Database Error"

        flash(error)

    return render_template("auth/register.html")


# Login
@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        user = db.session.get(User, username)

        if user is None:
            error = "User not found"

        elif not check_password_hash(user.password, password):
            error = "Incorrect Password"

        else:
            session.clear()
            session["user"] = user.username
            return redirect(url_for("urls.index"))

        if error is not None:
            flash(error)

    return render_template("auth/login.html")


# Logout
@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("urls.index"))
