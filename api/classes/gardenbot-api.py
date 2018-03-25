import os, sys
dirname = os.path.dirname(__file__)
gardenbot_file = os.path.join(dirname, '..', '..')
sys.path.append(gardenbot_file)
from gardenbot import Gardenbot
import time
from flask import Response
import authservice
import json
import pandas as pd

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
    soil_is_wet = Gardenbot.soil_is_wet()
    gb.close()
    msg = "{}".format(soil_is_wet)
    return Response(msg)


"""Returns a list of list with [date, number of waterings]"""
@authservice.requires_token
def get_data():
    logs = get_logs()
    logs = sanitize_logs(logs)
    df = convert_dataframe(logs)
    df = df.reset_index().values.tolist()
    return json.dumps(df)


@authservice.requires_token
def get_water_status():
    gb = Gardenbot()
    gb.setup_pins()
    return str(gb.enough_water())


def convert_dataframe(data):
    df = pd.DataFrame(data)
    df.columns = ['Date', 'Watering']
    df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d %H:%M:%S")
    df['Date'] = df['Date'].apply(lambda x: x.date())
    df['Date'] = df['Date'].apply(lambda x: date_to_seconds(x))
    df = df.groupby("Date").sum()
    return df


def sanitize_logs(json_object):
    for item in json_object:
        if str(item[1]).__contains__("INFO: Wet enough"):
            item[1] = 0
        else:
            item[1] = 1
    return json_object


"""Returns the log entries of the past 5 days as json object"""


def get_logs():
    with open("/home/pi/gardenbot/gardenbot.log") as f:
        lines = f.readlines()[-60:]
        lines = reversed(lines)
        return list((line.split(";") for line in lines))


"""Converts a datetime object to the number of seconds since the unix epoch."""


def date_to_seconds(d):
    return int(time.mktime(d.timetuple()))


@authservice.requires_token
def get_water_status():
    gb = Gardenbot()
    gb.setup_pins()
    return json.dumps(gb.enough_water())

