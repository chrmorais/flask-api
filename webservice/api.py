# coding: utf-8

from flask import request
from flask.ext import restful


from main import app
from models import Person


api = restful.Api(app)


class PersonAPI(restful.Resource):
    def get(self):
        limit = request.args.get('limit', 0)
        persons_list = Person.persons_list(limit)
        return {'persons': persons_list, 'limit': limit}

    def post(self, facebook_id):
        return {'message': 'ok'}

    def delete(self, facebook_id):
        return {'message': 'ok'}


api.add_resource(PersonAPI, '/person/')
