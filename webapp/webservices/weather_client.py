from pprint import pprint
import requests

city_id = 2885657
base_url = "http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={APIKEY}"

# s = "http://api.openweathermap.org/data/2.5/forecast/city?id={id}&APPID={APIKEY}".format(APIKEY="79e49fb1bc94e6f20e03087f81e4bb5e", id=2885657)
url = base_url.format(APIKEY="79e49fb1bc94e6f20e03087f81e4bb5e", city_id=2885657)
print(url)
# r = requests.get(s)
# pprint(r.json())
