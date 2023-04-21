from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    username = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String, nullable=False)
