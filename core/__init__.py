from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_restful import Api
from celery import Celery

from .config import Config
from apps import route_views

__all__ = ["app", "api", "db", "Config", "celery"]

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

celery = Celery(
    app.name, broker=app.config["CELERY_BROKER_URL"], include=["apps.records.tasks"]
)

SWAGGER_TEMPLATE = {
    "securityDefinitions": {
        "APIKeyHeader": {"type": "apiKey", "name": "Authorization", "in": "header"}
    }
}
Swagger(app, template=SWAGGER_TEMPLATE)

db = SQLAlchemy(app)

route_views()
