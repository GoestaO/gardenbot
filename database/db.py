from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys, os, datetime
from database.models import Protocol

CURRENT_WORK_DIR = os.path.dirname(__file__)
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_WORK_DIR, os.pardir))

sys.path.append(CURRENT_WORK_DIR)
sys.path.append(APPLICATION_DIR)
sys.path.append("/home/pi/gardenbot")

SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/{1}'.format(APPLICATION_DIR, 'gardenbot.db')
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


def persist(entity):
    session = Session()
    session.add(entity)
    session.commit()
    session.close()


def get_water_history_from_db():
    session = Session()
    sql = "SELECT date(protocol.timestamp), " \
          "count(protocol.water) " \
          "FROM protocol " \
          "GROUP BY date(protocol.timestamp) " \
          "ORDER BY date(protocol.timestamp) " \
          "ASC limit 5;"
    result = session.execute(sql).fetchall()
    session.close()
    return result




