import os
import requests
import yaml
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)


def _read_config():
    with open('api.conf') as config_file:
        conf = yaml.load(config_file)
    return conf


configuration = _read_config()

GARDENBOT_API_KEY = _read_config().get('gardenbot').get('key')
URL = _read_config().get('gardenbot').get('url')
header = {'Content-Type': 'application/json', 'Accept': 'application/problem+json',
           'API-Key': GARDENBOT_API_KEY}


def water_plants(seconds):
    url = "{}/watering/{}".format(URL, str(seconds))
    r = requests.post(url=url, headers=header)
    return r


'''Checks, if the soil is wet enough'''


def check():
    url = "{}check".format(URL)
    r = requests.post(url=url, headers=header)
    return r.text


"""Retrieves the watering history from the gardenbot"""


def get_water_history():
    url = "{}water_history".format(URL)
    r = requests.get(url=url, headers=header)
    return r.json()


"""Retrieves the sensordata history from the gardenbot"""


def get_sensordata_history():
    url = "{}sensordata_history".format(URL)
    r = requests.get(url=url, headers=header)
    return r.json()


def get_water_status():
    url = "{}waterstatus".format(URL)
    r = requests.get(url=url, headers=header)
    return r.json()


def get_sensor_data():
    url = "{}sensordata".format(URL)
    r = requests.get(url=url, headers=header)
    return r.json()

if __name__ == "__main__":
    json = get_sensor_data()
    print(json)
