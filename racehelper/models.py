"""
Storage! How do we store things?
"""

from sqlalchemy import Integer, DateTime, Column, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

from racehelper import str_format

__author__ = 'kenny'


Base = declarative_base()



class Race(Base):
    __tablename__ = 'race'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    type = Column(String(16))
    start_time = Column(DateTime)
    location_name = Column(String(64))
    location_google_term = Column(String(64))
    distance = Column(Float)
    description = Column(String(128))


class RaceRepository(object):

    def __init__(self, session):
        self._session = session

    def add_race(self, race):
        self._session.add(race)
        self._session.commit()

    def get_all(self):
        return self._session.query(Race).order_by(Race.id)


class RaceFactory(object):
    """
    Creates a race from a dictionary of attributes that gets passed in
    """

    def make_race(self, **attrs):
        #name, start_date, location_name,
        #          location_google_term, distance_str, description):

        attrs2 = {}
        for k,v in attrs.iteritems():
            attrs2[k.lower()] = v

        start_date = attrs2['date']
        distance_str = attrs2['distance']
        name = attrs2['name']
        location_name = attrs2['location']
        location_google_term = attrs2.get('locationsearchterm')
        type = attrs2['type']

        start_datetime = str_format.date_from_string(start_date)

        try:
            distance = _normalise_distance(distance_str)
        except:
            distance = None

        return Race(
            name=name,
            type=type,
            start_time=start_datetime,
            location_name=location_name,
            location_google_term=location_google_term,
            distance=distance,
        )





def _normalise_distance(s):
    """
    Converts a string into a distance in km

    :param s: Distance expressed as a string
    :return: Distance in kilometers
    """
    if s.endswith('m'):
        return float(s[:-1])*1.609

    if s.endswith('k'):
        return float(s[:-1])

    if s.lower() == 'marathon':
        return 42.2

    if s.lower() == 'half-marathon':
        return 21.1

    raise ValueError("Couldn't work out distance from string: %s" % s)