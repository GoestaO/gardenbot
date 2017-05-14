from app import app
from flask import render_template, request, redirect, url_for, flash
from forms import WaterForm, LoginForm
from app import login_manager
from flask import g, session
from models import User
from flask_login import current_user, login_user, logout_user, login_required
from webservice_clients import water_plants, check

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def homepage():
    form = WaterForm()
    return render_template('homepage.html', form=form)


@app.route('/water')
def water():
    if current_user.is_authenticated:
        form = WaterForm(request.form)
        return render_template('water.html', form=form)
    return redirect(url_for('login'))


@app.route('/status')
def status():
    soil_is_wet = check()
    return render_template("status.html", soil_is_wet=soil_is_wet)


@app.route('/water', methods=['POST'])
@login_required
def water_manually():
    form = WaterForm(request.form)
    if form.validate():
        time = request.form.get('wateringTime')
        r = water_plants(time)
        if r.status_code == 200:
            flash(r.text)
        return redirect(url_for('water'))
    # else:
    #     form = WaterForm()
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

