__author__ = 'kenny'

import unittest
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from racehelper.models import Race, Base



def make_race(name, datestr):
    return Race(
        name='example race',
        start_time=datetime.strptime(datestr, '%d-%b-%Y'),
    )

class TestRacePersistence(unittest.TestCase):

    def test_race(self):
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(make_race(name='example race', datestr='01-Jun-2016'))
        session.commit()

        expected = ['example race']

        returned = []
        for instance in session.query(Race).order_by(Race.id):
            returned.append(instance.name)

        self.assertEquals(expected, returned)


    def test_race_location(self):
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        datestr='01-Jun-2016'
        race = Race(
            name='example race',
            start_time=datetime.strptime(datestr, '%d-%b-%Y'),
            location_name='example location 1',
            location_google_term='asdf1234'
        )
        session.add(race)
        session.commit()

        expected = 'example location 1'
        returned = race.location_name
        self.assertEquals(expected, returned)

        expected = 'asdf1234'
        returned = race.location_google_term
        self.assertEquals(expected, returned)
