import falcon
import json
from api_services.audio_manager import save_audio, delete_audio, get_audio, update_audio
from api_services.custom_error_handler import error_handler

app = falcon.App()

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