from webservices import gardenbot_client
import pandas as pd
import datetime as dt

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
    df['Date'] = df['Date'].apply(lambda x: dt.datetime.strftime(x, '%Y-%m-%d'))
    df = df.groupby("Date").sum()

    print(df.to_records().tolist())

    #print(counts)

    #return counts
    #return pd.DataFrame.to_json(counts)




if __name__ == "__main__":
    data = get_data()
    json = convert_dataframe(data=data)
    print(json)

