import falcon, psycopg2
import json

def dberror_handler(ex, req, resp, params):
    if isinstance(ex, psycopg2.DatabaseError):
        resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
def error_handler(ex, req, resp, params):
    # Ignore HTTPError and re-raise
    if isinstance(ex, falcon.HTTPNotFound):
        resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
    elif isinstance(ex, falcon.HTTPInternalServerError):
        resp.text,resp.status = json.dumps({"Any Error": "500 internal server error"}), falcon.HTTP_500
    elif isinstance(ex, falcon.HTTPMethodNotAllowed):
        resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
    elif isinstance(ex, falcon.HTTPBadRequest):
        resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
    elif isinstance(ex, falcon.HTTPUnsupportedMediaType):
        resp.text,resp.status = json.dumps({"The request is invalid": "400 bad request"}), falcon.HTTP_400
    elif isinstance(ex, Exception):
        resp.text,resp.status = json.dumps({"Any Error": "500 internal server error"}), falcon.HTTP_500