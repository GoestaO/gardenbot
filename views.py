from app import app
from flask import render_template, request, redirect, url_for
from forms import WaterForm
from flask import flash

@app.route('/')
def homepage():
    form = WaterForm()
    return render_template('homepage.html', form=form)

@app.route('/', methods=['POST'])
def test_form():
    form = WaterForm(request.form)
    if form.validate():
        data = request.form.get('wateringTime')
        print(data)
        return redirect(url_for('homepage'))
    # else:
    #     form = WaterForm()
    return render_template('homepage.html', form=form)


