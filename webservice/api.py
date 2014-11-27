# coding: utf-8

from flask import request
from flask.ext import restful

from webservice.main import app
from webservice.models import Person
from webservice.services import Facebook
from webservice.exceptions import UserNotFound

api = restful.Api(app)


class PersonAPI(restful.Resource):
    def get(self):
        limit = request.args.get('limit', 0)
        persons_list = Person.persons_list(limit)
        return {'persons': persons_list, 'limit': limit}

    def post(self):
        facebook_id = request.form.get('facebookId', None)

        if facebook_id is None:
            return {'error': 'You must sent facebookId'}, 400

        try:
            user_data = Facebook.get_user_data(facebook_id=facebook_id)
        except UserNotFound:
            return {'error': 'Invalid facebookId'}, 404

        return {'message': 'ok'}

    def delete(self, facebook_id):
        return {'message': 'ok'}


api.add_resource(PersonAPI, '/person/')
