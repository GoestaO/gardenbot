from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URI = 'sqlite:///gardenbot.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)


def persist(entity):
    session = Session()
    session.add(entity)
    session.commit()
    session.close()






