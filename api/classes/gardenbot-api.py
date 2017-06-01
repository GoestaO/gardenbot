from garden import Gardenbot
import time
from flask import Response
import authservice
import json


@authservice.requires_token
def water_plants(seconds):
    gb = Gardenbot()
    gb.setup_pins()
    gb.close_water()
    watering_time = int(seconds)
    gb.water_plants(watering_time)
    gb.close()
    msg = "The plants have been watered for {0} seconds".format(seconds)
    return Response(msg)


@authservice.requires_token
def check_moisture():
    gb = Gardenbot()
    gb.setup_pins()
    gb.start_sensor()
    time.sleep(1)
    soil_is_wet = Gardenbot.soil_is_wet(14)
    gb.stop_sensor()
    gb.close()
    msg = "{}".format(soil_is_wet)
    return Response(msg)


@authservice.requires_token
def get_data():
    with open("/home/pi/gardenbot/gardenbot.log") as f:
        lines = f.readlines()[-60:]
        lines = reversed(lines)
        return json.dumps(list((line.split(";") for line in lines)))


