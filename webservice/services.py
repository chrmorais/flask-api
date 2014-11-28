# coding: utf-8

import json
import requests

from webservice.exceptions import UserNotFound


class Facebook(object):
    API_URL = 'https://graph.facebook.com/{facebook_id}'

    @staticmethod
    def get(url):
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        return

    @classmethod
    def get_user_data(cls, facebook_id):
        user_data = cls.get(cls.API_URL.format(facebook_id=facebook_id))

        if user_data is None:
            raise UserNotFound('User with this facebook_id %s not found.' % facebook_id)

        return {
            'username': user_data['username'],
            'facebook_id': user_data['id'],
            'name': user_data['name'],
            'gender': user_data['gender']
        }
