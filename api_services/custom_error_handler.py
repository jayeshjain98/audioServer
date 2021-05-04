import falcon
import json

def error_handler(ex, req, resp, params):
    # Ignore HTTPError and re-raise
    if isinstance(ex, falcon.HTTPNotFound):
        resp.body,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
    elif isinstance(ex, falcon.HTTPInternalServerError):
        resp.body,resp.status = json.dumps({"Any Error": "500 internal server error"}), falcon.HTTP_500
    elif isinstance(ex, falcon.HTTPMethodNotAllowed):
        resp.body,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
    elif isinstance(ex, falcon.HTTPBadRequest):
        resp.body,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
    elif isinstance(ex, Exception):
        resp.body,resp.status = json.dumps({"Any Error": "500 internal server error"}), falcon.HTTP_500