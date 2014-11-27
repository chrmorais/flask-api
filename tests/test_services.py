# coding: utf-8

import json
import mock

from webservice.services import Facebook
from webservice.exceptions import UserNotFound

from tests.base import BaseTestCase


class FacebookServiceTestCase(BaseTestCase):
    @mock.patch('webservice.services.requests')
    def test_get_method_return_none_when_response_is_404(self, request_mock):
        request_mock.get.return_value = mock.Mock(status_code=404)
        self.assertEqual(None, Facebook.get('http://localhost/'))

    @mock.patch('webservice.services.requests')
    def test_get_method_return_json_data_when_response_is_200(self, request_mock):
        request_mock.get.return_value = mock.Mock(status_code=200,
                                                  text=json.dumps({'message': 'ok'}))
        response = Facebook.get('http://localhost/')
        self.assertEqual('ok', response['message'])

    @mock.patch.object(Facebook, 'get')
    def test_invalid_facebook_id_raises_exception(self, facebook_mock):
        facebook_mock.return_value = None

        with self.assertRaises(UserNotFound):
            Facebook.get_user_data('123')

    @mock.patch.object(Facebook, 'get')
    def test_valid_facebook_id_return_correct_user_data(self, facebook_mock):
        facebook_mock.return_value = {
            'id': '123123',
            'username': 'username.test',
            'name': 'test',
            'gender': 'male'
        }

        data = Facebook().get_user_data('123123')
        self.assertEqual('username.test', data['username'])
