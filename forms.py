import wtforms
from wtforms.validators import DataRequired, NumberRange


class WaterForm(wtforms.Form):
    wateringTime = wtforms.IntegerField('Time (in seconds)', id='time',
                                        validators=[DataRequired(), NumberRange(min=1, max=120)])
    # key = wtforms.PasswordField('API-Key', id='api_key', validators=[DataRequired()])
    # ===========================================================================
    # def save_watering(self, watering):
    #     return watering
    # ===========================================================================


class LoginForm(wtforms.Form):
    email = wtforms.StringField("E-Mail: ", validators=[DataRequired()])
    password = wtforms.PasswordField("Password: ", validators=[DataRequired])
    remember_me = wtforms.BooleanField("Remember me?",
                                       default=True)

    def validate(self):
        if not super(LoginForm, self).validate():
            return False
        self.user = User.authenticate(self.email.data, self.password.data)
        if not self.user:
            self.email.errors.append("Invalid email or password.")
            return False
        return True
