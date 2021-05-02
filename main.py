
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
from services.audio_manager import save_audio, delete_audio

app = falcon.API()

write_handler = save_audio()
delete_handler = delete_audio()

app.add_route("/savefile",write_handler)
app.add_route("/{audioFileType}/{audioFileID:uuid}",delete_handler)