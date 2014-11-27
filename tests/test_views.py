# coding: utf-8

import json

from mixer.backend.flask import mixer
import mock

from webservice.exceptions import UserNotFound
from webservice.main import db
from webservice.models import Person

from tests.base import BaseTestCase


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
    @mock.patch('webservice.api.Facebook')
    def test_valid_facebook_id_should_create_person(self, facebook_mock):
        facebook_mock.get_user_data.return_value = {
            'facebook_id': '123123',
            'username': 'username.test',
            'name': 'test',
            'gender': 'male'
        }

        self.assertEqual(0, Person.query.count())

        response = self.client.post('/person/', data={'facebookId': '123123'})

        self.assertEqual(201, response.status_code)
        self.assertEqual(1, Person.query.count())

    @mock.patch('webservice.api.Facebook')
    def test_invalid_facebook_id_should_fail(self, facebook_mock):
        facebook_mock.get_user_data.side_effect = UserNotFound

        response = self.client.post('/person/', data={'facebookId': '123123'})
        self.assertEqual(404, response.status_code)


class PersonDeleteTestCase(BaseTestCase):
    def test_invalid_facebook_id_should_return_404(self):
        pass

    def test_valid_facebook_id_should_delete_person(self):
        pass
