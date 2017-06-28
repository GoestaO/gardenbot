from webservices import gardenbot_client
import pandas as pd
import datetime as dt
import time
from pprint import pprint
import json
from datetime import datetime


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


def convert_string_to_datetime_date(string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S").date()

def date_to_millis(d):
    """Converts a datetime object to the number of milliseconds since the unix epoch."""
    return int(time.mktime(d.timetuple()) * 1000)


if __name__ == "__main__":
    # logs = get_logs()
    # logs = sanitize_logs(logs)
    # print(logs)
    # df = convert_dataframe(logs)
    # print(df)
    test_list = [['2017-06-09 05:40:02', 1], ['2017-06-09 05:20:02', 1], ['2017-06-09 05:00:03', 0],
                 ['2017-06-09 04:40:02', 0], ['2017-06-09 04:20:03', 0], ['2017-06-09 04:00:02', 1],
                 ['2017-06-09 03:40:03', 1], ['2017-06-09 03:20:02', 0], ['2017-06-09 03:00:03', 0],
                 ['2017-06-09 02:40:02', 1], ['2017-06-09 02:20:02', 1], ['2017-06-09 02:00:03', 1],
                 ['2017-06-08 05:40:03', 1], ['2017-06-08 05:20:02', 1], ['2017-06-08 05:00:03', 1],
                 ['2017-06-08 04:40:02', 1], ['2017-06-08 04:20:03', 1], ['2017-06-08 04:00:03', 1],
                 ['2017-06-08 03:40:02', 1], ['2017-06-08 03:20:03', 1], ['2017-06-08 03:00:02', 1],
                 ['2017-06-08 02:40:03', 0], ['2017-06-08 02:20:02', 1], ['2017-06-08 02:00:03', 1],
                 ['2017-06-07 05:40:03', 0], ['2017-06-07 05:20:02', 0], ['2017-06-07 05:00:02', 1],
                 ['2017-06-07 04:40:02', 0], ['2017-06-07 04:20:03', 0], ['2017-06-07 04:00:02', 0],
                 ['2017-06-07 03:40:02', 1], ['2017-06-07 03:20:02', 0], ['2017-06-07 03:00:02', 1],
                 ['2017-06-07 02:40:03', 0], ['2017-06-07 02:20:02', 1], ['2017-06-07 02:00:03', 0],
                 ['2017-06-06 05:40:02', 0], ['2017-06-06 05:20:03', 0], ['2017-06-06 05:00:02', 0],
                 ['2017-06-06 04:40:03', 0], ['2017-06-06 04:20:02', 0], ['2017-06-06 04:00:02', 0],
                 ['2017-06-06 03:40:02', 0], ['2017-06-06 03:20:03', 0], ['2017-06-06 03:00:02', 0],
                 ['2017-06-06 02:40:02', 1], ['2017-06-06 02:20:02', 1], ['2017-06-06 02:00:02', 1],
                 ['2017-06-05 05:40:03', 0], ['2017-06-05 05:20:02', 0], ['2017-06-05 05:00:02', 0],
                 ['2017-06-05 04:40:02', 0], ['2017-06-05 04:20:03', 0], ['2017-06-05 04:00:02', 0],
                 ['2017-06-05 03:40:02', 0], ['2017-06-05 03:20:02', 0], ['2017-06-05 03:00:02', 0],
                 ['2017-06-05 02:40:03', 0], ['2017-06-05 02:20:02', 0], ['2017-06-05 02:00:03', 0]]

    test_list_modified = map(lambda x: [convert_string_to_datetime_date(x[0]), x[1]], test_list)
    df = convert_dataframe(list(test_list_modified))
    print(df)
    # pprint(list(test_list_modified))