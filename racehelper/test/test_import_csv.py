"""
Tests to make sure that we are able to successfully import races from a csv file.
"""

import unittest
from pkgutil import get_data
from cStringIO import StringIO

from racehelper.importers import load_tsv_races
__author__ = 'kenny'


def load_sample_races():
    data = get_data("racehelper.test.resources", "2016races.tsv")
    data_stream = StringIO(data)
    return load_tsv_races(data_stream)

class TestImportCsv(unittest.TestCase):

    def test_import1(self):
        """
        Import a sample set of races and check that they have been imported correctly
        :return:
        """
        races = list(load_sample_races())

        expected_name = "Chicken Run"
        self.assertEquals(expected_name, races[0].name)

        expected_len = 149
        self.assertEquals(expected_len, len(races))

