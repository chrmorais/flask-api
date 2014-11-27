# coding: utf-8
from flask.ext.testing import TestCase

from webservice.main import create_app, db


class BaseTestCase(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        self.app = create_app(self)
        return self.app

    def setUp(self):
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
