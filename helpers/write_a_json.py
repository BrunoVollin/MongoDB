import json
from bson import json_util
from datetime import datetime


def writeAJsonWithTime(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    now = datetime.now()
    dt_string = now.strftime("%H-%M-%S")

    with open(f"./json/{name} {dt_string}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))


def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))
