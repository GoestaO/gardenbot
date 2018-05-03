from flask import Flask, g
from configuration import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Configuration)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)
login_manager.login_view = "login"

bcrypt = Bcrypt(app)


@app.before_request
def _before_request():
    g.user = current_user


