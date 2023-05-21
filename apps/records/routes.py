from core import api
from .views import RecordResource


def route_views():
    api.add_resource(RecordResource, "/record/")
