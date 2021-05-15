import icalendar
from datetime import timedelta

def make_ical(concerts):
    cal = icalendar.Calendar()
    cal.add('prodid', '-//Concerts//jonnylamb.com//')
    cal.add('version', '2.0')
    cal.add('x-wr-calname', 'London Classical Concerts')
    cal.add('x-wr-caldesc', 'London Classical Concerts')
    cal.add('x-published-ttl', 'PT23H')
    cal.add('x-wr-timezone', 'Europe/London')

    for item in concerts:
        e = icalendar.Event()
        e.add('summary', item.title)
        e.add('dtstart', item.datetime)
        e.add('dtend', item.datetime + timedelta(hours=2, minutes=30))
        e.add('description', item.details)
        e.add('location', item.location)
        e.add('url', item.url)
        cal.add_component(e)

    return cal.to_ical()
