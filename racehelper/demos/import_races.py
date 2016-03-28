"""
Example use-case
"""
import os.path
from os.path import abspath, isfile, isdir, dirname

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from racehelper.importers import load_tsv_races
from racehelper.reports import make_tabular_report
from racehelper.models import Race, Base

__author__ = 'kenny'

def import_(args):
    from optparse import OptionParser

    parser = OptionParser()

    parser = OptionParser()
    parser.add_option('-f', '--file', dest='infile')
    parser.add_option('-d', '--data', dest='data')

    options, _ = parser.parse_args(args)

    if not os.path.isfile(options.data):
        parent_dir = abspath(dirname(options.data))
        assert isdir(parent_dir), 'Error locating data: %s' % abspath(options.data)


    new_db = not isfile(options.data)
    engine = create_engine('sqlite:///%s' % options.data)

    if new_db:
        Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    with open(options.infile) as f_in:
        for race in load_tsv_races(f_in):
            session.add(race)
        session.commit()

def print_races(args):
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option('-d', '--data', dest='data')
    options,_ = parser.parse_args(args)

    assert isfile(options.data)
    engine = create_engine('sqlite:///%s' % options.data)
    Session = sessionmaker(bind=engine)
    session = Session()

    print make_tabular_report(session.query(Race).order_by(Race.start_time))


if __name__ == '__main__':
    import sys

    dispatch = {
        'import': import_,
        'print': print_races,
    }
    cmd = sys.argv[1]
    dispatch[cmd](sys.argv[2:])