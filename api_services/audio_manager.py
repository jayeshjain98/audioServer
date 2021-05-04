import json
import falcon
from falcon.media.validators import jsonschema
from utilities.load_schema import validate_audio_input


class save_audio(object):
    """The class handles post request to save 3 different types of audio files in database"""

    @jsonschema.validate(validate_audio_input) 
    def on_post(self, req, resp):
        data = req.media
        resp.body,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200

class delete_audio(object):
    """The class handles delete request to delete 3 different types of audio files from database"""


    def on_delete(self, req, resp, audioFileID, audioFileType):
        if audioFileType in ["Song", "Podcast", "Audiobook"]:
            resp.body,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200
        else:
            resp.body,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400

class update_audio(object):
    """The class handles update request to update 3 different types of audio files in database"""

    @jsonschema.validate(validate_audio_input) 
    def on_put(self, req, resp, audioFileType, audioFileID):
        if audioFileType in ["Song", "Podcast", "Audiobook"]:
            data = req.media
            print(data)
            resp.body,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200
        else:
            resp.body,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400

class get_audio(object):
    """The class handles get request to fetch 3 different types of audio files from database"""


    def on_get(self, req, resp, audioFileType, audioFileID = None):
        if audioFileType in ["Song", "Podcast", "Audiobook"]:
            resp.body,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200
        else:
            resp.body,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
            