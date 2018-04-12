import os
import sys
sys.path.append('..')
from core.sensor import MiFloraSensor
from core.gardenbot import Gardenbot
from database.db import get_water_history_from_db
from flask import Response
from classes import authservice
import json


@authservice.requires_token
def water_plants(seconds):
    gb = Gardenbot()
    gb.close_water()
    watering_time = int(seconds)
    gb.water_plants(watering_time)
    msg = "The plants have been watered for {0} seconds".format(seconds)
    return Response(msg)


@authservice.requires_token
def check_moisture():
    sensor = MiFloraSensor()
    sensor_data = json.loads(sensor.get_miflora_data())
    soil_is_wet = Gardenbot.soil_is_wet(sensor_data)
    msg = "{}".format(soil_is_wet)
    return Response(msg)


"""Returns a list of list with [date, number of waterings]"""
@authservice.requires_token
def water_history():
    return json.dumps([tuple(row) for row in get_water_history_from_db()])

@authservice.requires_token
def get_water_status():
    gb = Gardenbot()
    return str(gb.enough_water())


@authservice.requires_token
def get_water_status():
    gb = Gardenbot()
    gb.setup_pins()
    return json.dumps(gb.enough_water())
