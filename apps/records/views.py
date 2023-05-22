from flasgger import swag_from
from flask_restful import Resource
from flask import send_from_directory, request
from core import Config
from core.bases import decorators
from apps.users.decorators import authorize_decorator
from .models import AudioFile, db
from .tasks import convert_file


class RecordResource(Resource):
    method_decorators = (authorize_decorator, decorators.exception_catcher_decorator)

    @swag_from(Config.SWAGGER_FORMS + "record_get.yml")
    def get(self):
        audio_file = AudioFile.query.filter_by(
            id=request.args["id"], owner_id=request.user.id
        ).first()
        if audio_file is None:
            return "File is not found, or you don't have access", 404
        if not audio_file.converted:
            return "The file has not been converted yet", 425
        return send_from_directory(Config.UPLOAD_FOLDER, f'{request.args["id"]}.mp3')

    @swag_from(Config.SWAGGER_FORMS + "record_post.yml")
    def post(self):
        if request.files["file"].filename.split(".")[-1] != "wav":
            return ".wav file format required.", 400

        audio_file = AudioFile(owner_id=request.user.id)
        db.session.add(audio_file)
        db.session.commit()
        request.files["file"].save(Config.UPLOAD_FOLDER + f"{audio_file.id}.wav")
        convert_file.delay(str(audio_file.id))
        return f"{request.base_url}?id={audio_file.id}&user={request.user.id}", 201
