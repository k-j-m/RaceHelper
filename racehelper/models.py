"""
Storage! How do we store things?
"""

from sqlalchemy import Integer, DateTime, Column, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'kenny'


Base = declarative_base()


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    google_search_term = Column(String(64))


class Race(Base):
    __tablename__ = 'race'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    start_time = Column(DateTime)
    #location_id = Column(Integer, ForeignKey("location.id"))
    #location = relationship("Location")

