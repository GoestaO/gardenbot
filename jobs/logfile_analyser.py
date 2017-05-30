from pprint import pprint
import json


def get_data(filename):
    with open(filename) as f:
        lines = f.readlines()[-60:]
        lines = reversed(lines)
        return json.dumps(list((line.split(";") for line in lines)))


json_object = get_data("gardenbot.log")
pprint(json_object)