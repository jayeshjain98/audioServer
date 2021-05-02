import json
import falcon
from falcon.media.validators import jsonschema
from utilities.load_schema import validate_audio_input


class save_audio(object):
    """The class handles post request to save 3 different types of audio file"""
    # __json_content = {}

    # def __validate_json_input(self, req):
    #     try:
    #         self.__json_content = json.loads(req.stream.read())
    #         print("json from client is validated! :)")
    #         return True

    #     except ValueError as e:
    #         self.__json_content = {}
    #         print('json from client is not validted :(')
    #         return False
    @jsonschema.validate(validate_audio_input) 
    def on_post(self, req, resp):
        try:
            # validated = self.__validate_json_input(req)
            data = req.media
            resp.body,resp.status = json.dumps({"Action is successful" : "200 OK"}), falcon.HTTP_200
        except:
            resp.body,resp.status = json.dumps({"Any error" : "500 Internal Server Error"}), falcon.HTTP_500