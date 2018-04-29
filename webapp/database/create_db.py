from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys


from sqlalchemy import create_engine
CURRENT_WORK_DIR = os.path.dirname(__file__)
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_WORK_DIR, os.pardir))

sys.path.append(CURRENT_WORK_DIR)
sys.path.append(APPLICATION_DIR)
from models import Protocol, Base
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/{1}'.format(APPLICATION_DIR, 'gardenbot.db')

if __name__ == "__main__":
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)