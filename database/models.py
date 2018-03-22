from sqlalchemy import Column, Integer, BigInteger, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()


class Protocol(Base):
    id = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    temperature = Column(Integer)
    moisture = Column(Integer)
    fertility = Column(Integer)
    water = Column(Boolean)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<Timestamp: {0}; Seconds: {1}'.format(self.watering_timestamp, self.duration)