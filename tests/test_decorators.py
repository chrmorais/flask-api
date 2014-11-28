# coding: utf-8

import mock

from webservice.decorators import facebook_id_required

from tests.base import BaseTestCase


class FacebookIDRequiredTestCase(BaseTestCase):
    def setUp(self):
        self.decorated_function = facebook_id_required(lambda *args, **kwargs: kwargs)

    @mock.patch('webservice.decorators.request')
    def test_request_without_facebook_id_should_return_error(self, request_mock):
        request_mock.form.get.return_value = None
        response, status_code = self.decorated_function()

        self.assertEqual('You must sent facebook_id.', response['error'])
        self.assertEqual(400, status_code)

    @mock.patch('webservice.decorators.request')
    def test_request_with_facebook_id_should_inject(self, request_mock):
        request_mock.form.get.return_value = '123123'
        response = self.decorated_function()

        self.assertEqual('123123', response['facebook_id'])
