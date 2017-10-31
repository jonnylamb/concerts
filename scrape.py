#!/usr/bin/env python

from collections import namedtuple
from datetime import datetime

Concert = namedtuple('Concert', ['title', 'datetime', 'location', 'details', 'url'])

locations = {
    'BH': 'Barbican Hall',
    'CH': 'Cadogan Hall',
    'KP': 'Kings Place',
    'MC': 'Milton Court',
    'GHG': 'Great Hall, Goldsmiths College',
    'QEH': 'Queen Elizabeth Hall',
    'RAH': 'Royal Albert Hall',
    'RFH': 'Royal Festival Hall',
    'OG': 'Giulio Potenza',
    'JL': 'Jackson Lane',
    'SJSS': 'St John\'s Smith Square',
    'MTH': 'Merchants\' Taylor Hall',
    'SMTF': 'St Martin in The Fields',
    'TH': 'Trinity House',
    'WH': 'Wigmore Hall'
}

def is_bottom(tag):
    return tag.name == 'p' and tag.get('class') == 'Bottom'

def process_row(row):
    data = row.findAll('td')

    # why do we have go to through this?
    location_code = data[0].text
    location = locations.get(location_code, location_code)

    details = data[1]
    title = details.find('p').text

    date_cell = details.find(is_bottom)
    datetime_str = date_cell.find('time').get('datetime')
    parsed_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

    details_str = '\n'.join([
        s.text.encode('utf-8') for s in details.findAll('p')[1:-1] if len(s.text) > 0
    ])

    url = data[-1].find('a').get('href')

    # google calendar doesn't use the url field so just throw it in here as well
    details_str += '\n\n' + url.encode('iso-8859-1')

    return Concert(
        title=title,
        datetime=parsed_datetime,
        location=location,
        details=details_str,
        url=url
    )

def is_datarow(tag):
    # Row1-0 is weird top row which should be ignored
    return tag.name == 'tr' \
        and tag.get('id') \
        and tag.get('id').startswith('Row1-') \
        and tag.get('id') != 'Row1-0'

def find_concerts(soup):
    all_rows = soup.findAll(is_datarow)

    return map(process_row, all_rows)
