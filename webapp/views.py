from app import app
from flask import render_template, request, redirect, url_for, flash, jsonify, Response, session
from forms import WaterForm, LoginForm
from app import login_manager
from models import User
from flask_login import current_user, login_user, logout_user, login_required
from webservices import gardenbot_client, weather_client
import datetime, time

testdata = {'name': 'Flower care', 'firmware': '3.1.8', 'conductivity': 547, 'battery': 99, 'moisture': 21, 'temperature': 23.7, 'light': 3410}


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def homepage():
    # current_weather = weather_client.get_current_weather()
    # weather_icon_url = weather_client.get_weather_icon_url(weather_client.get_weather_icon(current_weather))
    return render_template('homepage.html')


@app.route('/water', methods=['GET'])
@login_required
def water():
    response = gardenbot_client.water_plants(30)
    return jsonify(response.text, response.status_code)


@app.route("/status", methods=['GET'])
@login_required
def status():
    soil_is_wet = gardenbot_client.check()
    return soil_is_wet


@app.route("/sensordata", methods=['GET'])
@login_required
def sensordata():
    sensor_data = gardenbot_client.get_sensor_data()
    return jsonify(sensor_data)


@app.route("/waterstatus", methods=['GET'])
@login_required
def water_status():
    water_level = gardenbot_client.get_water_status()
    return str(water_level)


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


def convert_dataframe(data):
    df = pd.DataFrame(data)
    df.columns = ['Date', 'Watering']
    df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d %H:%M:%S")
    df['Date'] = df['Date'].dt.date
    df['Date'] = df['Date'].apply(lambda x: date_to_millis(x))
    df = df.groupby("Date").sum()
    plot_data = df.reset_index().values.tolist()
    return plot_data


def date_to_millis(date_string):
    dateobject = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    """Converts a datetime object to the number of milliseconds since the unix epoch."""
    return int(time.mktime(dateobject.timetuple()) * 1000)


@app.route("/history")
def show_history():
    plot_data = gardenbot_client.get_water_history()

    chartID = 'chart_ID'
    chart_type = 'line'
    chart_height = 350
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height}
    series = [{"data": plot_data, "showInLegend": "false"}]

    title = {"text": 'Watering activities'}
    xAxis = {"type": "datetime", "tickInterval": 24 * 3600 * 1000}
    yAxis = {"title": {"text": 'Count'}, "tickInterval": 1}
    return render_template('history.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis,
                           yAxis=yAxis, plot_data=plot_data)


