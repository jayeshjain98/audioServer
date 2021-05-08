# audioServer
A rest api developed using falcon framework in python and PostgreSQL database. The app helps in managing audio files metadata over the server.
# install PostgreSQL
To set up database on ubuntu follow the link https://www.postgresql.org/download/linux/ubuntu/ 
# set up environment
```bash
pip3 install -r requirements.txt
```
# create tables 
The **databaseschema.py** file creates 3 tables namely music_files, podcast_records and audiobook_library. 
```bash
python3 database_services/schema/databaseschema.py
```
# serve the api
This shell command will serve the api on your localhost over port 8000
```bash
gunicorn --workers 1 --timeout 60 -b 0.0.0.0:8000 main:app
```
# request url and format
The api takes request at four end points in below format
* Create -http://127.0.0.1:8000/savefile
* Delete -http://127.0.0.1:8000/deletefile/{audioFileType}/{audioFileID}
* Update -http://127.0.0.1:8000/updatefile/{audioFileType}/{audioFileID}
* Get -http://127.0.0.1:8000/getfile/{audioFileType}/{audioFileID} or http://127.0.0.1:8000/getfile/{audioFileType}
The format for create and update api request is as follows
for Song:
```json
{
  "audioFileType": "Song",
  "audioMetadata": {
    "song_upload_time": "2018-01-18T00:00:00",
    "song_id": "2EB8AA08-AA98-11EA-B4AA-73B441D16380",
    "song_name": "abcd",
    "song_duration": 1
  }
}
```
for Podcast:
```json
{
  "audioFileType": "Podcast",
  "audioMetadata": {
    "podcast_upload_time": "2018-01-18T00:00:00",
    "podcast_id": "2EB8AA08-AA98-11EA-B4AA-73B441D16380",
    "podcast_name": "abcd",
    "podcast_duration": 1,
    "host": "abc",
    "participants": [
      "jack"
    ]
  }
}
```
for Audiobook:
```json
{
  "audioFileType": "Audiobook",
  "audioMetadata": {
    "audiobook_upload_time": "2018-01-18T00:00:00",
    "audiobook_id": "2EB8AA08-AA98-11EA-B4AA-73B441D16380",
    "audiobook_title": "abcd",
    "audiobook_duration": 1,
    "author": "abc",
    "narrator": "jack"
  }
}
```
