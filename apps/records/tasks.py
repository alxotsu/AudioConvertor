from pydub import AudioSegment
from core import Config
from .models import db


def convert_file(file_stream, audio_file):
    sound = AudioSegment.from_wav(file_stream)
    sound.export(f"{Config.UPLOAD_FOLDER}{audio_file.id}.mp3", format="mp3")

    audio_file.converted = True
    db.session.add(audio_file)
    db.session.commit()
