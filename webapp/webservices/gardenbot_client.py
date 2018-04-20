import requests
import sys
sys.path.extend('..')
from configuration import Configuration

base_url_local = 'http://gardenbot.local/v1.0/'

API_KEY = Configuration.GARDENBOT_API_KEY
header = {'Content-Type': 'application/json', 'Accept': 'application/problem+json',
           'API-Key': API_KEY}

print(header)
base_url_test = 'http://gardenbot.local/v1.0/'
base_url_remote = "https://797e6e7778.dataplicity.io/v1.0/"

URL = base_url_test

def water_plants(seconds):
    url = "{}/watering/{}".format(URL, str(seconds))
    r = requests.post(url=url, headers=header)
    return r


'''Checks, if the soil is wet enough'''


def check():
    url = "{}check".format(URL)
    r = requests.post(url=url, headers=header)
    # text = check()
    # print(text)
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

if __name__ == "__main__":
    json = get_water_status()
    print(json)
