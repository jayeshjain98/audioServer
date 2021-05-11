import psycopg2

def create_connection(user='postgres',host='127.0.0.1',password='12345',port='5432',database="audio_store"):
    connection = None
    try:
        connection = psycopg2.connect("user={} host={} password={} port={} dbname={}".format(user,host,password,port,database))    
    except Exception as e:
        print(e)
    return connection

def create_database():
    database_created="F"
    connection=psycopg2.connect("user='postgres' host='127.0.0.1'password='12345'port='5432'")
    
    if connection is not None:
        connection.autocommit = True
    
        cur = connection.cursor()
    
        cur.execute("SELECT datname FROM pg_database;")
    
        list_database = cur.fetchall()
        database_name = "audio_store"
    
        if (database_name,) in list_database:
            print("create_database::database exist!!")
            database_created="T"
        else:
            try:
                cur.execute('CREATE DATABASE audio_store')
                database_created="T"
                print("create_database::database created!!")
            except:
                print('DatabaseSchema:Database not created.')
        connection.close()
        return database_created
        

def create_tables():
    b=create_database()
    if b == "T":
        connection=create_connection()
        cur = connection.cursor()
        try:
            cur.execute("DROP TABLE IF EXISTS music_files;")
            cur.execute("DROP TABLE IF EXISTS podcast_records;")
            cur.execute("DROP TABLE IF EXISTS audiobook_library;")

            cur.execute("CREATE TABLE music_files ( song_id VARCHAR(40) NOT NULL, song_name VARCHAR(100) NOT NULL, song_duration INT NOT NULL, upload_time VARCHAR(30) NOT NULL, PRIMARY KEY(song_id));")

            print("DatabaseSchema: music_files table created")

            cur.execute("CREATE TABLE podcast_records ( podcast_id VARCHAR(40) NOT NULL, podcast_name VARCHAR(100) NOT NULL, podcast_host VARCHAR(100) NOT NULL, podcast_duration INT NOT NULL, participants_1 VARCHAR(100) DEFAULT NULL, participants_2 VARCHAR(100) DEFAULT NULL, participants_3 VARCHAR(100) DEFAULT NULL, participants_4 VARCHAR(100) DEFAULT NULL, participants_5 VARCHAR(100) DEFAULT NULL, participants_6 VARCHAR(100) DEFAULT NULL, participants_7 VARCHAR(100) DEFAULT NULL, participants_8 VARCHAR(100) DEFAULT NULL, participants_9 VARCHAR(100) DEFAULT NULL, participants_10 VARCHAR(100) DEFAULT NULL, podcast_time VARCHAR(30) NOT NULL, PRIMARY KEY(podcast_id));")

            print("DatabaseSchema: podcast_records table created")

            cur.execute("CREATE TABLE audiobook_library ( audiobook_id VARCHAR(40) NOT NULL, audiobook_title VARCHAR(100) NOT NULL, audiobook_author VARCHAR(100) NOT NULL, audiobook_narrator VARCHAR(100) NOT NULL, audiobook_duration INT NOT NULL, upload_time VARCHAR(30) NOT NULL, PRIMARY KEY(audiobook_id));")

            print("DatabaseSchema: audiobook_library table created")
            
        except Exception as e:
            print("Databaseschema:{}".format(e))
        connection.commit()
        connection.close()
        cur.close()


#call function to create database as well as tables   
if __name__ == "__main__":

    create_tables()
                
