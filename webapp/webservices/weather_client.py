from pprint import pprint
import requests
import sys
sys.path.extend('..')
from configuration import Configuration



city_id = 7290255
API_KEY = Configuration.OPENWEATHER_API_KEY


def get_current_weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={APIKEY}&units=metric"
    url = base_url.format(APIKEY=API_KEY, city_id=city_id)
    r = requests.get(url)
    json = r.json()
    return json


def get_weather_icon(weather):
    return weather.get("weather").pop().get("icon")


def get_weather_icon_url(icon_id):
    base_url = "http://openweathermap.org/img/w/{}.png"
    return base_url.format(icon_id)


if __name__ == '__main__':
    current_weather = get_current_weather()
    pprint(current_weather.get("main")['temp'])
    # weather_icon = current_weather.get("weather").pop().get("icon")
    # pprint(weather_icon.pop().get("icon"))
    # image_url = get_weather_icon(weather_icon)
    # pprint(image_url)
    # print(weather_icon)
