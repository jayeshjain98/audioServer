import database_services.operation.db_operationutil as ops
from database_services.operation import db_query
import psycopg2

operation = {
            "get" : ops.get,
            "insert" : ops.insert,
            "delete" : ops.delete,
            "update" : ops.update
            
            }

db_query_mapper = {"get" : {"Song": db_query.fetch_song, "Podcast" : db_query.fetch_podcast, "Audiobook" : db_query.fetch_audiobook},
                    "delete" : {"Song": db_query.delete_song, "Podcast" : db_query.delete_podcast, "Audiobook" : db_query.delete_audiobook},
                    "insert" : {"Song": db_query.insert_song, "Podcast" : db_query.insert_podcast, "Audiobook" : db_query.insert_audiobook},
                    "update" : {"Song": db_query.update_song, "Podcast" : db_query.update_podcast, "Audiobook" : db_query.update_audiobook}}

class dbUtil(object):
    """The utilty file that handles database methods """
    
    get = "get"
    insert = "insert"
    delete = "delete"
    update = "update"
    
    
    def doOperation(operationname, parameters, filetype):
        """Call appropriate method from operationutil """
        try:
            if operationname == 'get' and parameters[0] == None:
                if filetype == 'Song':
                    query = db_query.fetchall_song
                elif filetype == 'Podcast':
                    query = db_query.fetchall_podcast
                elif filetype == 'Audiobook':
                    query = db_query.fetchall_audiobook
            elif operationname == 'get' and parameters[0] != None:
                query = db_query_mapper[operationname][filetype]
                query = (query %parameters)
            else:
                query = db_query_mapper[operationname][filetype]
            result = operation[operationname](parameters, query)
            return result
        except Exception as error :
            raise error
