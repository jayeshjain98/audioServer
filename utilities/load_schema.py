import json


def get_schema(json_resource):
    with open(json_resource, 'r') as file:
        return json.load(file)
    
validate_audio_input = get_schema("./schema/validate_audio_input.json")