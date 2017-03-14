import connexion
from flask import g
from configuration import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bcrypt import Bcrypt

app = connexion.App(__name__)
app.add_api('api/endpoints/gardenbot-api.yaml')
app.app.config.from_object(Configuration)
db = SQLAlchemy(app.app)
migrate = Migrate(app.app, db)
manager = Manager(app.app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app.app)
login_manager.login_view = "login"

bcrypt = Bcrypt(app.app)


@app.app.before_request
def _before_request():
    g.user = current_user


# @app.app.before_request
# def csrf_protect():
#     if request.method == "POST":
#         token = session.pop('_csrf_token', None)
#         if not token or token != request.form.get('_csrf_token'):
#             abort(403)
#
# def generate_csrf_token():
#     if '_csrf_token' not in session:
#         session['_csrf_token'] = '000b3d18-7f83-4515-ab66-99199cbbd074'
#     return session['_csrf_token']

# app.app.jinja_env.globals['csrf_token'] = generate_csrf_token


if __name__ == "__main__":
    app = connexion.App(__name__)
    app.add_api('endpoints/gardenbot-api.yaml')
    app.run(port=8080)
