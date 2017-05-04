from app import app
from flask import render_template, request, redirect, url_for, flash
from forms import WaterForm, LoginForm
from app import login_manager
from flask import g
from models import User
from flask_login import current_user, login_user, logout_user, login_required


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def homepage():
    form = WaterForm()
    return render_template('homepage.html', form=form)


@app.route('/', methods=['POST'])
@login_required
def water_manually():
    form = WaterForm(request.form)
    if form.validate():
        time = request.form.get('wateringTime')
        flash("Watering started for {0} seconds".format(time))
        return redirect(url_for('homepage'))
    # else:
    #     form = WaterForm()
    return render_template('homepage.html', form=form)


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
