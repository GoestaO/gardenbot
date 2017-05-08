import requests

base_url = 'http://gardenbot.local/v1.0/'
headers = {'Content-Type': 'application/json', 'Accept': 'application/problem+json',
           'API-Key': '000b3d18-7f83-4515-ab66-99199cbbd074'}

base_url_test = 'http://gardenbot.local:5000/v1.0/'


def water_plants(seconds):
    url = "{}/watering/{}".format(base_url, str(seconds))
    r = requests.post(url=url, headers=headers)
    return r


'''Checks, if the soil is wet enough'''
def check():
    header = {'Content-Type': 'application/json', 'Accept': 'Accept: text/html',
               'API-Key': '000b3d18-7f83-4515-ab66-99199cbbd074'}
    url = "{}check".format(base_url)
    r = requests.post(url=url, headers=header)
    return r.text

if __name__ == "__main__":
    # text = check()
    # print(text)
    water_plants(5)
