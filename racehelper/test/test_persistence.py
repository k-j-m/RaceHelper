__author__ = 'kenny'

import unittest
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from racehelper.models import Race, Base, Location


def add_test_locations(session):
    session.add(Location(name='example location 1', google_search_term="asdf1234"))
    session.add(Location(name='example location 2', google_search_term="asdf1234"))
    session.add(Location(name='example location 3', google_search_term="asdf1234"))


class TestRacePersistence(unittest.TestCase):

    def test_race(self):
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        race = Race(
            name='example race',
            start_time=datetime.strptime('01-Jun-2016', '%d-%b-%Y'),
        )
        session.add(race)
        session.commit()

        print race.id

        expected = ['example race']

        returned = []
        for instance in session.query(Race).order_by(Race.id):
            returned.append(instance.name)

        self.assertEquals(expected, returned)


    def test_store_location(self):
        engine = create_engine('sqlite:///:memory:', echo=False)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        add_test_locations(session)
        session.commit()

        expected = [
            'example location 1',
            'example location 2',
            'example location 3',
        ]

        returned = []
        for instance in session.query(Location).order_by(Location.id):
            returned.append(instance.name)

        self.assertEquals(expected, returned)