"""
Make sure that we can safely mung a number of string formats into the data
that they represent.
"""
import unittest
import datetime

import str_format

__author__ = 'kenny'

class TestDates(unittest.TestCase):
    """
    Make sure that we can correctly read a date from a string.
    """

    def test_date1(self):
        date_str = '19-Mar-16'

        expected_date = datetime.datetime(2016, 03, 19)
        returned_date = str_format.date_from_string(date_str)
        self.assertEquals(expected_date, returned_date)