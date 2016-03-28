"""
Shake down the RaceFactory class to make sure that it is suitably robust in the inputs that
it can accept.
"""

import unittest
from itertools import izip
from racehelper.models import RaceFactory

__author__ = 'kenny'

class TestFactory(unittest.TestCase):
    """
    Tests to demonstrate the robustness of the RaceFactory class
    """
    race_factory = RaceFactory()

    def test_example1(self):
        """
        Example using sample data from my original google sheets spreadsheet.
        https://docs.google.com/spreadsheets/d/13ntlk4ai2Lkq-c1Xx5g8my2Z6QjBEHIt7fHRQbcWSbA/edit#gid=0&fvid=1978454132
        :return:
        """


        header = """Weekday	Date	Type	Name	Location	Description	Distance	Link	Distance (km)	Headbanger	Championship	Handicap	Driving Time (hrs from clubhouse)"""
        data = """Sat	19-Mar-16	Fell	Chicken Run	Hayfield	BS fell race	5.8m	http://fellrunner.org.uk/races.php?id=4580	9.3322				1.25"""
        race_attributes = dict(izip(
            header.split('\t'),
            data.split('\t')
        ))
        race = self.race_factory.make_race(**race_attributes)

        expected_name = 'Chicken Run'
        returned_name = race.name

        self.assertEquals(expected_name, returned_name)