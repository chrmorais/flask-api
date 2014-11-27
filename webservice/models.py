# coding: utf-8


from main import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facebook_id = db.Column(db.Integer, index=True, unique=True)
    username = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    def __init__(self, facebook_id, username, name, gender):
        self.facebook_id = facebook_id
        self.username = username
        self.name = name
        self.gender = gender

    def __repr__(self):
        return '<Person %r>' % (self.name)

    @classmethod
    def persons_list(cls, limit=None):
        persons = []

        query = cls.query.limit(limit) if limit else cls.query

        for person in query.all():
            persons.append({
                'username': person.username,
                'facebookId': person.facebook_id,
                'name': person.name,
                'gender': person.gender
            })
        return persons

    @staticmethod
    def save_person(facebook_id, username, name, gender):
        person = Person(facebook_id, username, name, gender)
        db.session.add(person)
        db.session.flush()
