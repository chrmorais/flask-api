# coding: utf-8

from flask.ext.script import Manager
from webservice.main import db, create_app


manager = Manager(create_app)


@manager.command
def create_tables():
    from webservice.models import Person
    db.create_all()


if __name__ == '__main__':
    manager.run()
