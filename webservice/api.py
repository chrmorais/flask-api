# coding: utf-8

from flask import request
from flask.ext import restful

from webservice.exceptions import UserNotFound
from webservice.main import app
from webservice.models import Person
from webservice.services import Facebook

api = restful.Api(app)


class PersonListAPI(restful.Resource):
    def get(self):
        limit = request.args.get('limit', 0)
        persons_list = Person.persons_list(limit)
        return {'persons': persons_list, 'limit': limit}


class PersonAPI(restful.Resource):
    def post(self, facebook_id):
        try:
            user_data = Facebook.get_user_data(facebook_id=facebook_id)
        except UserNotFound:
            return {'error': 'Invalid facebookId.'}, 404

        Person.save_person(**user_data)
        return {'message': 'ok'}, 201

    def delete(self, facebook_id):
        try:
            Person.delete_person(facebook_id=facebook_id)
        except UserNotFound:
            return {'error': 'Invalid facebookId.'}, 404
        return {'message': 'ok'}, 204


api.add_resource(PersonListAPI, '/person/')
api.add_resource(PersonAPI, '/person/<int:facebook_id>')
