from webservices import gardenbot_client
import pandas as pd
import datetime as dt
import time
from pprint import pprint
import json


def convert_dataframe(data):
    df = pd.DataFrame(data)
    df.columns = ['Date', 'Watering']
    df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d %H:%M:%S")
    # df['Date'] = df['Date'].apply(lambda x: date_to_millis(x))
    df['Date'] = df['Date'].apply(lambda x: x.date())
    df['Date'] = df['Date'].apply(lambda x: date_to_millis(x))
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
    with open("gardenbot.log") as f:
        lines = f.readlines()[-60:]
        lines = reversed(lines)
        return list((line.split(";") for line in lines))


def date_to_millis(d):
    """Converts a datetime object to the number of milliseconds since the unix epoch."""
    return int(time.mktime(d.timetuple()))


if __name__ == "__main__":
    logs = get_logs()
    logs = sanitize_logs(logs)
    df = convert_dataframe(logs)
    print(df)
