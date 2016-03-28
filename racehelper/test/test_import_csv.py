"""
Tests to make sure that we are able to successfully import races from a csv file.
"""

import unittest
from pkgutil import get_data
from cStringIO import StringIO

from racehelper.importers import load_tsv_races
__author__ = 'kenny'


class TestImportCsv(unittest.TestCase):

    def test_import1(self):
        """
        Import a sample set of races and check that they have been imported correctly
        :return:
        """
        data = get_data("racehelper.test.resources", "2016races.tsv")
        data_stream = StringIO(data)
        races = load_tsv_races(data_stream)

        expected_name = "Chicken Run"
        returned_name = races[0].name
        self.assertEquals(expected_name, returned_name)