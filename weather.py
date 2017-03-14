from pprint import pprint
import requests


s = "http://api.openweathermap.org/data/2.5/forecast/city?id={id}&APPID={APIKEY}".format(APIKEY="79e49fb1bc94e6f20e03087f81e4bb5e", id=2950159)
r = requests.get(s)
pprint(r.json())
