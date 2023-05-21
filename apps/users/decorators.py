from flask import request
from .models import User
from core.bases.exceptions import AuthError


def authorize_decorator(method):
    def inner(*args, **kwargs):
        user_id = request.args.get("user")
        token = request.headers.get('Authorization', None)

        try:
            user = User.query.filter_by(id=int(user_id), token=token).first()
        except Exception:
            raise AuthError()
        if user is None:
            raise AuthError()

        request.user = user

        return method(*args, **kwargs)
    return inner
