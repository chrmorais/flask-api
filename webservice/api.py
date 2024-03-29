# coding: utf-8

from flask import request
from flask.ext import restful

from webservice.decorators import facebook_id_required
from webservice.exceptions import UserNotFound, UserFound
from webservice.main import app, logger
from webservice.models import Person
from webservice.services import Facebook


api = restful.Api(app)


class PersonListAPI(restful.Resource):
    def get(self):
        limit = request.args.get('limit', 0)
        persons_list = Person.persons_list(limit)
        return {'persons': persons_list, 'limit': limit}

    @facebook_id_required
    def post(self, facebook_id):
        try:
            user_data = Facebook.get_user_data(facebook_id=facebook_id)
        except UserNotFound:
            logger.error('POST /person/ facebook_id={} - Invalid facebook_id'.format(facebook_id))
            return {'error': 'Invalid facebook_id.'}, 404

        try:
            Person.save_person(**user_data)
            logger.info('POST /person/ facebook_id={} - Successul inserted'.format(facebook_id))
        except UserFound:
            logger.error('POST /person/ facebook_id={} - Already inserted'.format(facebook_id))
            return {'error': 'User already inserted.'}, 400

        return {'message': 'ok'}, 201


class PersonAPI(restful.Resource):
    def delete(self, facebook_id):
        try:
            Person.delete_person(facebook_id=facebook_id)
            logger.info('DELETE /person/{} - Successul deleted'.format(facebook_id))
        except UserNotFound:
            logger.error('DELETE /person/{} - Invalid facebook_id'.format(facebook_id))
            return {'error': 'Invalid facebook_id.'}, 404

        return {}, 204


api.add_resource(PersonListAPI, '/person/')
api.add_resource(PersonAPI, '/person/<int:facebook_id>')
