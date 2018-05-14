import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CURRENT_DIR = os.path.dirname(__file__)
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
sys.path.append(CURRENT_DIR)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/{1}'.format(CURRENT_DIR, 'gardenbot.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://gardenbot:gardenbot@localhost:3306/gardenbot'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


def persist(entity):
    session = Session()
    session.add(entity)
    session.commit()
    session.close()


def get_water_history_from_db():
    session = Session()
    sql = "select * from (SELECT UNIX_TIMESTAMP(timestamp(date(protocol.timestamp), '02:00:00'))*1000 as millis, " \
          "count(protocol.water) as waterings FROM protocol " \
          "GROUP BY date(protocol.timestamp) " \
          "ORDER BY date(protocol.timestamp) " \
          "desc limit 5)sub order by sub.millis asc;"
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
