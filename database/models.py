from sqlalchemy import Column, Integer, BigInteger, DateTime, Boolean, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import datetime

Base = declarative_base()


class SensorData(Base):
    __tablename__ = 'sensordata'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    timestamp = Column(DateTime(timezone=True), default=datetime.datetime.now)
    temperature = Column(Float)
    moisture = Column(Integer)
    fertility = Column(Integer)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<Timestamp: {0}; temperature: {1}; moisture: {2}; fertility: {3}'.format(self.timestamp,
                                                                                         self.temperature,
                                                                                         self.moisture,
                                                                                         self.fertility)


class Protocol(Base):
    __tablename__ = 'protocol'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    timestamp = Column(DateTime(timezone=True), default=datetime.datetime.now)
    water = Column(Boolean, default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return '<Timestamp: {0}; Water: {1}'.format(self.timestamp, self.water)
