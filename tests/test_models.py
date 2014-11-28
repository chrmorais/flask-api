# coding: utf-8

from mixer.backend.flask import mixer

from webservice.main import db
from webservice.models import Person

from tests.base import BaseTestCase


class PersonModelTestCase(BaseTestCase):
    def create_persons(self, number=3):
        persons = mixer.cycle(number).blend(Person)
        map(db.session.add, persons)
        db.session.flush()
        return persons

    def test_person_list_return_all_persons(self):
        persons = self.create_persons()

        expected_list = []

        for person in persons:
            expected_list.append({
                'username': person.username,
                'facebookId': person.facebook_id,
                'name': person.name,
                'gender': person.gender
            })

        persons_list = Person.persons_list()
        self.assertEqual(expected_list, persons_list)

    def test_person_list_with_limit_return_only_2_persons(self):
        self.create_persons(3)
        persons_list = Person.persons_list(limit=2)
        self.assertEqual(2, len(persons_list))

    def test_save_person_add_person_in_db(self):
        data = {'facebook_id': '123', 'username': 'username',
                'name': 'name_test', 'gender': 'male'}

        self.assertEqual(0, Person.query.count())
        Person.save_person(**data)
        self.assertEqual(1, Person.query.count())

    def test_delete_person_should_remove_person_from_db(self):
        persons = self.create_persons(1)
        self.assertEqual(1, Person.query.count())
        Person.delete_person(persons[0].facebook_id)
        self.assertEqual(0, Person.query.count())
