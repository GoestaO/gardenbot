import wtforms
from wtforms.validators import DataRequired, NumberRange


class WaterForm(wtforms.Form):
    wateringTime = wtforms.IntegerField('Time (in seconds)', id='time',
                                        validators=[DataRequired(), NumberRange(min=1, max=120)])
    #key = wtforms.PasswordField('API-Key', id='api_key', validators=[DataRequired()])
    def save_watering(self, watering):
        return watering
