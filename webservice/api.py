# coding: utf-8

from flask import request
from flask.ext import restful

from webservice.decorators import facebook_id_required
from webservice.exceptions import UserNotFound
from webservice.main import app
from webservice.models import Person
from webservice.services import Facebook

api = restful.Api(app)


class PersonAPI(restful.Resource):
    def get(self):
        limit = request.args.get('limit', 0)
        persons_list = Person.persons_list(limit)
        return {'persons': persons_list, 'limit': limit}

    @facebook_id_required
    def post(self, facebook_id):
        try:
            user_data = Facebook.get_user_data(facebook_id=facebook_id)
        except UserNotFound:
            return {'error': 'Invalid facebookId'}, 404

        return {'message': 'ok'}

    @facebook_id_required
    def delete(self, facebook_id):
        return {'message': 'ok'}


api.add_resource(PersonAPI, '/person/')
