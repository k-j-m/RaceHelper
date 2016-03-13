"""
Storage! How do we store things?
"""

from sqlalchemy import Integer, DateTime, Column, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'kenny'


Base = declarative_base()



class Race(Base):
    __tablename__ = 'race'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    start_time = Column(DateTime)
    location_name = Column(String(64))
    location_google_term = Column(String(64))



class RaceRepository(object):

    def __init__(self, session):
        self._session = session

    def add_race(self, race):
        self._session.add(race)
        self._session.commit()
