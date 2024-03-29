# coding: utf-8

from sqlalchemy.orm.exc import NoResultFound

from webservice.exceptions import UserFound, UserNotFound
from webservice.main import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facebook_id = db.Column(db.Integer, index=True, unique=True)
    username = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    @classmethod
    def persons_list(cls, limit=None):
        persons = []

        query = cls.query.limit(limit) if limit else cls.query

        for person in query.all():
            persons.append({
                'username': person.username,
                'facebook_id': person.facebook_id,
                'name': person.name,
                'gender': person.gender
            })
        return persons

    @classmethod
    def delete_person(cls, facebook_id):
        try:
            person = cls.query.filter_by(facebook_id=facebook_id).one()
        except NoResultFound:
            raise UserNotFound()

        db.session.delete(person)
        db.session.commit()

    @staticmethod
    def save_person(facebook_id, username, name, gender):
        if Person.query.filter_by(facebook_id=facebook_id).first():
            raise UserFound()

        person = Person()
        person.facebook_id = facebook_id
        person.username = username
        person.name = name
        person.gender = gender

        db.session.add(person)
        db.session.commit()
