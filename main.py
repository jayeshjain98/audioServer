
# {
#   "audioFileType": "Song",
#   "audioMetadata": {
#     "song_upload_time": "2018-01-18T00:00:00",
#     "song_id": "2EB8AA08-AA98-11EA-B4AA-73B441D16380",
#     "song_name": "abcd",
#     "song_duration": 1
#   }
# }

# {
#   "audioFileType": "Podcast",
#   "audioMetadata": {
#     "podcast_upload_time": "2018-01-18T00:00:00",
#     "podcast_id": "2EB8AA08-AA98-11EA-B4AA-73B441D16380",
#     "podcast_name": "abcd",
#     "podcast_duration": 1,
#     "host": "abc",
#     "participants": [
#       "jack"
#     ]
#   }
# }

# {
#   "audioFileType": "Audiobook",
#   "audioMetadata": {
#     "audiobook_upload_time": "2018-01-18T00:00:00",
#     "audiobook_id": "2EB8AA08-AA98-11EA-B4AA-73B441D16380",
#     "audiobook_title": "abcd",
#     "audiobook_duration": 1,
#     "author": "abc",
#     "narrator": "jack"
#   }
# }
import falcon
import json
from api_services.audio_manager import save_audio, delete_audio, get_audio, update_audio
from api_services.custom_error_handler import error_handler

app = falcon.API()

write_handler = save_audio()
delete_handler = delete_audio()
update_handler = update_audio()
get_handler = get_audio()
app.add_error_handler(falcon.HTTPError, error_handler)

app.add_route("/savefile",write_handler)
app.add_route("/deletefile/{audioFileType}/{audioFileID:uuid}",delete_handler)
app.add_route("/updatefile/{audioFileType}/{audioFileID:uuid}",update_handler)
app.add_route("/getfile/{audioFileType}",get_handler)
app.add_route("/getfile/{audioFileType}/{audioFileID:uuid}",get_handler)