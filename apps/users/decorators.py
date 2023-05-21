from flask import request
from .models import User


def authorize_decorator(method):
    def inner(*args, **kwargs):
        user_id = request.args.get("user_id")
        token = request.headers.get('Authorization', None)

        if token is None or user_id is None:
            request.user = None
        else:
            request.user = User.query.filter_by(id=int(user_id), token=token).first()

        return method(*args, **kwargs)
    return inner
