#!/usr/bin/env python

from scrape import fetch_concerts
from ical import make_ical

if __name__ == '__main__':
    concerts = fetch_concerts()
    print(make_ical(concerts))
