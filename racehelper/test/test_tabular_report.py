"""
Test our tools for creating tabular reports
"""
import unittest

from racehelper.test.test_import_csv import load_sample_races
from racehelper.reports import make_tabular_report

__author__ = 'kenny'

class TestTabular(unittest.TestCase):

    def test_printout1(self):
        print make_tabular_report(load_sample_races())