from pprint import pprint
import requests

city_id = 2885657
APIKEY="79e49fb1bc94e6f20e03087f81e4bb5e"
# temp = json.get('main').get('temp')

def get_current_weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={APIKEY}&units=metric"
    url = base_url.format(APIKEY=APIKEY, city_id=city_id)
    r = requests.get(url)
    json = r.json()
    return json




