import requests

base_url_local = 'http://gardenbot.local/v1.0/'
headers = {'Content-Type': 'application/json', 'Accept': 'application/problem+json',
           'API-Key': 'a1c86893-841e-45c6-9f1f-f8a31a58d601'}

base_url_test = 'http://gardenbot.local:5000/v1.0/'
base_url_remote = "https://797e6e7778.dataplicity.io/v1.0/"


def water_plants(seconds):
    url = "{}/watering/{}".format(base_url_remote, str(seconds))
    r = requests.post(url=url, headers=headers)
    return r


'''Checks, if the soil is wet enough'''


def check():
    header = {'Content-Type': 'application/json', 'Accept': 'Accept: text/html',
              'API-Key': 'a1c86893-841e-45c6-9f1f-f8a31a58d601'}
    url = "{}check".format(base_url_remote)
    r = requests.post(url=url, headers=header)
    # text = check()
    # print(text)
    return r.text


"""Retrieves the watering history from the gardenbot"""

def get_history():
    header = {'Content-Type': 'application/json', 'Accept': 'Accept: application/json',
              'API-Key': 'a1c86893-841e-45c6-9f1f-f8a31a58d601'}
    url = "{}history".format(base_url_local)
    r = requests.get(url=url, headers=header)
    return r.json()


def get_water_status():
    header = {'Content-Type': 'application/json', 'Accept': 'Accept: application/json',
              'API-Key': 'a1c86893-841e-45c6-9f1f-f8a31a58d601'}
    url = "{}waterstatus".format(base_url_remote)
    r = requests.get(url=url, headers=header)
    return r.json()

if __name__ == "__main__":
    json = get_water_status()
    print(json)
