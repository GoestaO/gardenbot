import requests

base_url = 'http://gardenbot.local/v1.0/watering/'
headers = {'Content-Type': 'application/json', 'Accept': 'application/problem+json',
           'API-Key': '000b3d18-7f83-4515-ab66-99199cbbd074'}


def water_plants(seconds):
    url = "{}{}".format(base_url, str(seconds))
    r = requests.post(url=url, headers=headers)
    return r.text


water_plants(5)
