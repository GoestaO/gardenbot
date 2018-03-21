from pprint import pprint
import json
import os, sys
dirname = os.path.dirname(__file__)
gardenbot_file = os.path.join(dirname, '..', 'gardenbot.py')
sys.path.append(gardenbot_file)

def get_data(filename):
    with open(filename) as f:
        lines = f.readlines()[-60:]
        lines = reversed(lines)
        return json.dumps(list((line.split(";") for line in lines)))


# json_object = get_data("gardenbot.log")
# pprint(json_object)

if __name__ == '__main__':
    with open(gardenbot_file) as f:
        lines = f.readlines()
        pprint(lines)