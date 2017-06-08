from webservices import gardenbot_client
import pandas as pd
import datetime as dt
import time
from pprint import pprint
import json


def get_data():
    json = gardenbot_client.get_history()
    for item in json:
        if str(item[1]).__contains__("INFO: Wet enough"):
            item[1] = 0
        else:
            item[1] = 1
    return json


def convert_dataframe(data):
    df = pd.DataFrame(data)
    df.columns = ['Date', 'Watering']
    df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d %H:%M:%S")
    df['Date'] = df['Date'].dt.date
    df['Date'] = df['Date'].apply(lambda x: date_to_millis(x))
    df = df.groupby("Date").sum()
    return df


def date_to_millis(d):
    """Converts a datetime object to the number of milliseconds since the unix epoch."""
    return "{}".format(str(int(time.mktime(d.timetuple()))))


def convert_to_int(input):
    return int(input)


if __name__ == "__main__":
    data = get_data()
    # pprint(data)
    df = convert_dataframe(data=data)
    plotdata = df.reset_index().to_json(orient='split')
    #     i[0] = convert_to_int(i[0])
    # pprint(jsondata)
    # plot_data = json.load(jsondata)
    pprint(plotdata[4])
