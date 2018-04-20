import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CURRENT_DIR = os.path.dirname(__file__)
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
sys.path.append(CURRENT_DIR)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/{1}'.format(CURRENT_DIR, 'gardenbot.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///var/www/gardenbot-api/database/gardenbot.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


def persist(entity):
    session = Session()
    session.add(entity)
    session.commit()
    session.close()


def get_water_history_from_db():
    session = Session()
    sql = "SELECT strftime('%s', date(protocol.timestamp))*1000, " \
          "count(protocol.water) " \
          "FROM protocol " \
          "GROUP BY date(protocol.timestamp) " \
          "ORDER BY date(protocol.timestamp) " \
          "ASC limit 5;"
    result = session.execute(sql).fetchall()
    session.close()
    return result


def get_sensordata_from_db():
    session = Session()
    sql = "SELECT timestamp, temperature, moisture, fertility, light, battery from sensordata;"
    result = session.execute(sql).fetchall()
    session.close()
    return result


if __name__ == "__main__":
    print(SQLALCHEMY_DATABASE_URI)
    print(get_water_history_from_db())