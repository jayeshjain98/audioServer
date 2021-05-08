import json
import falcon
from falcon.media.validators import jsonschema
from database_services.operation.dbUtil import dbUtil
from api_services.json_parser import metadata_parser
from utilities.load_schema import validate_audio_input


class save_audio(object):
    """The class handles post request to save 3 different types of audio files in database"""

    @jsonschema.validate(validate_audio_input) 
    def on_post(self, req, resp):
            data = req.media
            filetype,parameters = metadata_parser(data)
            dbUtil.doOperation(dbUtil.insert,parameters,filetype)
            resp.text,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200


class delete_audio(object):
    """The class handles delete request to delete 3 different types of audio files from database"""

    def on_delete(self, req, resp, audioFileID, audioFileType):
        audioFileID = str(audioFileID).upper() if audioFileType != None else None
        if audioFileType in ["Song", "Podcast", "Audiobook"]:
            parameters = (audioFileID,)
            dbUtil.doOperation(dbUtil.delete,parameters,audioFileType)
            resp.text,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200
        else:
            resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400

class update_audio(object):
    """The class handles update request to update 3 different types of audio files in database"""

    # @jsonschema.validate(validate_audio_input) 
    def on_put(self, req, resp, audioFileType, audioFileID):
        # resp.text,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200
        if audioFileType in ["Song", "Podcast", "Audiobook"]:
            data = req.media
            filetype,parameters = metadata_parser(data)
            if audioFileType == filetype:
                dbUtil.doOperation(dbUtil.update,parameters[1:]+(str(audioFileID).upper(),),filetype)
                resp.text,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200
            else:
                resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
        else:
            resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400


class get_audio(object):
    """The class handles get request to fetch 3 different types of audio files from database"""

    def on_get(self, req, resp, audioFileType, audioFileID = None):
        audioFileID = str(audioFileID).upper() if audioFileID != None else None
        if audioFileType in ["Song", "Podcast", "Audiobook"]:
            parameters = (audioFileID,)
            result = dbUtil.doOperation(dbUtil.get,parameters,audioFileType)
            resp.text,resp.status = json.dumps({"filenames" : result}), falcon.HTTP_200
        else:
            resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
