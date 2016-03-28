"""
Module provides a number of different importers to be used for loading race data into memory from
some interchange medium.
"""
from racehelper.models import RaceFactory

__author__ = 'kenny'

def load_tsv_races(tsv_stream):
    """
    Loads race data from a tab-delimited file-like-object.

    The first row must contain column headers as expected by the RaceFactory class. To start
    with this function will use the RaceFactory statically, but this can be abstracted out
    if we ever want to have a generic tsv-loader than can instantiate multiple different types of
    object. This is not currently a requirement so has been left out.

    :param tsv_stream:
    :return: Iter[Race]
    """
    race_factory = RaceFactory()
    headers = next(tsv_stream).strip().split('\t')

    for line in tsv_stream:
        values = line.strip().split('\t')
        race_attributes = dict(zip(headers, values))
        new_race = race_factory.make_race(**race_attributes)
        yield new_race
