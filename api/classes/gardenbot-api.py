from garden import Gardenbot
import time
from flask import Response
import authservice
import json
import pandas as pd
from miflora.miflora_poller import MiFloraPoller
from miflora.backends.gatttool import GatttoolBackend
from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY


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


@authservice.requires_token
def get_miflora_data():
    poller = MiFloraPoller('C4:7C:8D:65:B5:CF', GatttoolBackend)
    d = dict()
    d['firmware'] = poller.firmware_version()
    d['name'] = poller.name()
    d['temperature'] = poller.parameter_value(MI_TEMPERATURE)
    d['moisture'] = poller.parameter_value(MI_MOISTURE)
    d['light'] = poller.parameter_value(MI_LIGHT)
    d['conductivity'] = poller.parameter_value(MI_CONDUCTIVITY)
    d['battery'] = poller.parameter_value(MI_BATTERY)
    return json.dumps(d)
