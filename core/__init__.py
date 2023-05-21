from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

from .config import Config
from apps import route_views

__all__ = ['app', 'db', 'Config']


app = Flask(__name__)
app.config.from_object(Config)
Swagger(app)

db = SQLAlchemy(app)

route_views()
