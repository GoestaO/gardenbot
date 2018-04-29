from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, sys


from sqlalchemy import create_engine
CURRENT_DIR = os.path.dirname(__file__)
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))

sys.path.append(CURRENT_DIR)
sys.path.append(APPLICATION_DIR)
from models import Protocol, Base
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/{1}'.format(CURRENT_DIR, 'gardenbot.db')

if __name__ == "__main__":
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)