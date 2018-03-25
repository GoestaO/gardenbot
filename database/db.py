from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys, os
CURRENT_WORK_DIR = os.getcwd()
APPLICATION_DIR = os.path.abspath(os.path.join(CURRENT_WORK_DIR, os.pardir))

sys.path.append(CURRENT_WORK_DIR)
sys.path.append(APPLICATION_DIR)


SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/{1}'.format(APPLICATION_DIR, 'gardenbot.db')
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)


def persist(entity):
    session = Session()
    session.add(entity)
    session.commit()
    session.close()






