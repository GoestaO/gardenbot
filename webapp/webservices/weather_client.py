from pprint import pprint
import requests

city_id = 7290255
APIKEY = "79e49fb1bc94e6f20e03087f81e4bb5e"


# temp = json.get('main').get('temp')


def get_current_weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={APIKEY}&units=metric"
    url = base_url.format(APIKEY=APIKEY, city_id=city_id)
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
    pprint(current_weather)
    # weather_icon = current_weather.get("weather").pop().get("icon")
    # pprint(weather_icon.pop().get("icon"))
    # image_url = get_weather_icon(weather_icon)
    # pprint(image_url)
    # print(weather_icon)
