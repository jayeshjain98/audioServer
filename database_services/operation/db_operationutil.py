import psycopg2
from database_services.operation.connection_pool import db_connection_pool


def get(parameters,query):
    """To fetch data from the database """
    try:
        conn=db_connection_pool.getconn()
        with conn.cursor() as cur:
            
            cur.execute(query)
            conn.commit()
            count = cur.rowcount
            if count == 0:
                raise psycopg2.DatabaseError()
            filenames = [row[0] for row in cur.fetchall()]
            cur.close()
        db_connection_pool.putconn(conn)
        return filenames

    except Exception as error:
        db_connection_pool.putconn(conn)
        raise error

        
        
        

def insert(parameters,query):
    """To insert data into the database """
    
    try:
        conn=db_connection_pool.getconn()
        with conn.cursor() as cur:

            cur.execute(query %parameters)
            conn.commit()
        db_connection_pool.putconn(conn)

    except psycopg2.DatabaseError as error:
        db_connection_pool.putconn(conn)
        raise error

            
def delete(parameters,query):
    """To delete records from the database """
    
    try:
        conn=db_connection_pool.getconn()
        with conn.cursor() as cur:
            query = (query %parameters)
            cur.execute(query)
            conn.commit()
        db_connection_pool.putconn(conn)

    except Exception as error:
        db_connection_pool.putconn(conn)
        raise error    

def update(parameters,query):
    """To delete records from the database """
    
    try:
        conn=db_connection_pool.getconn()
        with conn.cursor() as cur:
            query = (query %parameters)
            cur.execute(query)
            count = cur.rowcount
            if count == 0:
                raise psycopg2.DatabaseError()
            conn.commit()
        db_connection_pool.putconn(conn)

    except Exception as error:
        db_connection_pool.putconn(conn)
        raise error