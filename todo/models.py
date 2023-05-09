from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    username = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String, nullable=False)
    tasks = db.relationship("Task", backref="user", lazy="dynamic")


class Task(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String, db.ForeignKey("user.username"))
    task = db.Column(db.String, nullable=False)
    target_date = db.Column(db.Date)
    complete = db.Column(db.Boolean, default=False)
