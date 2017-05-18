import requests

base_url_local = 'http://gardenbot.local/v1.0/'
headers = {'Content-Type': 'application/json', 'Accept': 'application/problem+json',
           'API-Key': '000b3d18-7f83-4515-ab66-99199cbbd074'}

base_url_test = 'http://gardenbot.local:5000/v1.0/'
base_url_remote = "https://797e6e7778.dataplicity.io/v1.0/"

def water_plants(seconds):
    url = "{}/watering/{}".format(base_url_local, str(seconds))
    r = requests.post(url=url, headers=headers)
    return r


'''Checks, if the soil is wet enough'''
def check():
    header = {'Content-Type': 'application/json', 'Accept': 'Accept: text/html',
               'API-Key': '000b3d18-7f83-4515-ab66-99199cbbd074'}
    url = "{}check".format(base_url_local)
    r = requests.post(url=url, headers=header)
    # text = check()
    # print(text)
    return r.text

if __name__ == "__main__":
    water_plants(5)
