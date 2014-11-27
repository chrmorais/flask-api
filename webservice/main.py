# coding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = None


def create_app(config='settings'):
    global app, db

    if app is None:
        app = Flask(__name__)
        app.config.from_object(config)
        db.init_app(app)

        import api

    return app
