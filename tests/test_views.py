# coding: utf-8

import json

from mixer.backend.flask import mixer

from webservice.main import create_app, db
from webservice.models import Person

test_app = create_app()

from base import BaseTestCase


class PersonListTestCase(BaseTestCase):
    def create_persons(self, number=3):
        persons = mixer.cycle(number).blend(Person)
        map(db.session.add, persons)
        db.session.flush()
        return persons

    def test_person_list_should_return_200(self):
        response = self.client.get('/person/')
        self.assertEqual(200, response.status_code)

    def test_person_list_should_return_all_persons(self):
        self.create_persons(3)

        persons_list = Person.persons_list()
        response = self.client.get('/person/')
        data = json.loads(response.data)
        self.assertEqual(persons_list, data['persons'])

    def test_person_list_with_limit_return_correct_values(self):
        self.create_persons(3)
        response = self.client.get('/person/?limit=1')

        data = json.loads(response.data)
        self.assertEqual(1, len(data['persons']))

    def test_person_list_without_persons_return_empty_list(self):
        response = self.client.get('/person/')

        data = json.loads(response.data)
        self.assertEqual([], data['persons'])


class PersonInsertTestCase(BaseTestCase):
    def test_valid_facebook_id_should_create_person(self):
        pass

    def test_invalid_facebook_id_should_fail(self):
        pass

    def test_invalid_method_should_return_not_allowed(self):
        pass
