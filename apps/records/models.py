from core import db
import uuid


class AudioFile(db.Model):
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    converted = db.Column(db.Boolean, default=False, nullable=False)
    owner_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
