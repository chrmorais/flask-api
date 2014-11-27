# coding: utf-8

from flask import request
from functools import wraps


def facebook_id_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        facebook_id = request.form.get('facebookId', None)
        if facebook_id is None:
            return {'error': 'You must sent facebookId.'}, 400
        kwargs['facebook_id'] = facebook_id
        return func(*args, **kwargs)
    return wrapper
