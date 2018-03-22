import os, sys
import sqlalchemy
import yaml
from configuration import SQLALCHEMY_DATABASE_URI

db = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)

if __name__ == '__main__':
    db.create_all()
