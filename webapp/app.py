import os
from flask import Flask, Session, g
from configuration import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bcrypt import Bcrypt

application = Flask(__name__)
app = application
application.config.from_object(Configuration)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
manager = Manager(application)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(application)
login_manager.login_view = "login"

bcrypt = Bcrypt(application)


@application.before_request
def _before_request():
    g.user = current_user


