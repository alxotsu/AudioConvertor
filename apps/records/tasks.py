import os
from pydub import AudioSegment
from core import Config, celery, app
from .models import AudioFile, db


@celery.task
def convert_file(audio_file_id):
    filename = Config.UPLOAD_FOLDER + f"{audio_file_id}.wav"
    sound = AudioSegment.from_wav(filename)
    sound.export(f"{Config.UPLOAD_FOLDER}{audio_file_id}.mp3", format="mp3")
    os.remove(filename)

    with app.app_context():
        audio_file = AudioFile.query.filter_by(id=audio_file_id).first()
        audio_file.converted = True
        db.session.add(audio_file)
        db.session.commit()
