from core import db
import uuid


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(32), nullable=False)
    token = db.Column(db.UUID, default=uuid.uuid4)
