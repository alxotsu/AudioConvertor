from flasgger import swag_from
from flask_restful import Resource
from core import Config
from core.bases import decorators
from .models import User, db


class UserResource(Resource):
    method_decorators = (decorators.exception_catcher_decorator,)

    @swag_from(Config.SWAGGER_FORMS + 'user_post.yml')
    def post(self, username):
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return {'id': user.id, 'token': user.token.__str__()}, 201
