from app import app
from flask import render_template, request, redirect, url_for, flash, jsonify, Response
from forms import WaterForm, LoginForm
from app import login_manager
from flask import g, session
from models import User
from flask_login import current_user, login_user, logout_user, login_required
from webservices import gardenbot_client, weather_client
import pandas as pd
import datetime as dt
import time
from pandas_highcharts.core import serialize
from pandas.compat import StringIO


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def homepage():
    current_weather = weather_client.get_current_weather()
    weather_icon_url = weather_client.get_weather_icon_url(weather_client.get_weather_icon(current_weather))
    return render_template('homepage.html', current_weather=current_weather, weather_icon_url=weather_icon_url)


@app.route('/water', methods=['GET'])
def water():
    response = gardenbot_client.water_plants(30)
    return jsonify(response.text, response.status_code)


@app.route("/status", methods=['GET'])
def status() -> str:
    soil_is_wet = gardenbot_client.check()
    return soil_is_wet
    # return render_template("history.html", soil_is_wet=soil_is_wet)


@app.route('/waterManually', methods=['POST'])
@login_required
def water_manually():
    form = WaterForm(request.form)
    if form.validate():
        time = request.form.get('wateringTime')
        r = gardenbot_client.water_plants(time)
        if r.status_code == 200:
            flash(r.text)
        return redirect(url_for('water'))
    return render_template('water.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            login_user(form.user, remember=form.remember_me.data)
            flash("Successfully logged in as {}".format(form.user.email), "success")
            return redirect(request.args.get("next") or url_for("homepage"))
    else:
        form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(request.args.get("next") or url_for("homepage"))


@app.route("/get_history_data", methods=["GET"])
def get_history_data():
    json = gardenbot_client.get_history()
    for item in json:
        if str(item[1]).__contains__("INFO: Wet enough"):
            item[1] = "0"
        else:
            item[1] = "60"
    return jsonify(json)


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
    return "new Date({})".format(str(int(time.mktime(d.timetuple())) * 1000))


# @app.route("/history", methods=["GET"])
# def show_history():
#     # json = gardenbot_client.get_history()
#     # for item in json:
#     #     if str(item[1]).__contains__("INFO: Wet enough"):
#     #         item[1] = "0"
#     #     else:
#     #         item[1] = "60"
#     return render_template("history.html")


@app.route("/history")
def show_history():
    json = gardenbot_client.get_history()
    for item in json:
        if str(item[1]).__contains__("INFO: Wet enough"):
            item[1] = 0
        else:
            item[1] = 1

    plot_data = convert_dataframe(json)
    # chartID = 'chart_ID'
    # chart_type = 'line'
    # chart_height = 350
    # chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    # series = [{"data": plot_data}]
    #
    # title = {"text": 'Watering activities'}
    # xAxis = {"type": "datetime"}
    # yAxis = {"title": {"text": 'Watering count'}}
    chart = serialize(plot_data, render_to="my-chart", title="My Chart")

    # return render_template('history.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis,
    #                        yAxis=yAxis)


    return render_template("history.html", chart=chart)

# @app.route("/history")
# def show_history():
# json = gardenbot_client.get_history()
# for item in json:
#     if str(item[1]).__contains__("INFO: Wet enough"):
#         item[1] = 0
#     else:
#         item[1] = 1
#
# plot_data = convert_dataframe(json)
# chart = serialize(plot_data, render_to="my-chart", title="My Chart")
# dat = """ts;A;B;C
# 2015-01-01 00:00:00;27451873;29956800;113
# 2015-01-01 01:00:00;20259882;17906600;76
# 2015-01-01 02:00:00;11592256;12311600;48
# 2015-01-01 03:00:00;11795562;11750100;50
# 2015-01-01 04:00:00;9396718;10203900;43
# 2015-01-01 05:00:00;14902826;14341100;53"""
# df = pd.read_csv(StringIO(dat), sep=';', index_col='ts', parse_dates='ts')
#
# # Basic line plot
# chart = serialize(df, render_to="my-chart", title="My Chart")
#
# return render_template("history.html", chart=chart)
