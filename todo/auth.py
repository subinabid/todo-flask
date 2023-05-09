from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from todo.models import db, User

app = Blueprint("auth", __name__, url_prefix="/auth")


# Register a user
@app.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not username:
            flash("Username is required")

        elif not password:
            flash("Password is missing")

        else:
            try:
                u = User(username=username, password=generate_password_hash(password))
                db.session.add(u)
                db.session.commit()

            except Exception:
                flash("Some Error")

    return render_template("auth/register.html")


# Login
@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = db.session.get(User, username)

        if user is None:
            flash("User not found")

        elif not check_password_hash(user.password, password):
            flash("Incorrect Password")

        else:
            session.clear()
            session["user"] = user.username
            return redirect(url_for("urls.index"))

    return render_template("auth/login.html")


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("urls.index"))
