# coding: utf-8

import logging

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


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(handler)
    return logger


logger = create_logger()
