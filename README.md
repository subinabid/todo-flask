# TODO App!

## Installation

    $ pipenv install

## One time setup db

    $  flask --app todo shell

    >> from todo.models import db
    >> db.create_all()


## Run the app

   $ flask --app todo run

