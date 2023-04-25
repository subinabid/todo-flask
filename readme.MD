# SQL Alchemy usage

## installation
```pip install Flask-SQLAlchemy```


## Usage
- create models.py
- import SQLAlchemy ```from flask_sqlalchemy import SQLAlchemy```
- create a db instance ```db = SQLAlchemy()```
- create models inheriting ```db.Model```


## Initiate database (From Terminal)
- ```Flask --app appname shell ```
- ```from appname.models import db  ```
- ```db.create_all() ```
### Note:
- This cannot handle migrations