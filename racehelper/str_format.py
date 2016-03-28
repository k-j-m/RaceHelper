import dateparser

__author__ = 'kenny'

def date_from_string(date_str):
    """
    Converts a date string into a datetime value. This is currently a simple wrapper around
    the dateparser package.

    :param date_str:
    :return:
    """
    return dateparser.parse(date_str)