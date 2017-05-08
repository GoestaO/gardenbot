from garden import Gardenbot
import time
import connexion
from flask import Response
# from moisture import Gardenbot
import authservice


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
    msg = "Soil is wet: {}".format(soil_is_wet)
    return Response(msg)

