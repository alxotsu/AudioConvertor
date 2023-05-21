from core import api
from .views import UserResource


def route_views():
    api.add_resource(UserResource, "/user/<string:username>/")
