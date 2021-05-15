import boto3
import json

from scrape import fetch_concerts
from ical import make_ical

def lambda_handler(event, context):
    concerts = fetch_concerts()
    ical = make_ical(concerts)

    s3 = boto3.resource('s3')
    obj = s3.Object('files.jonnylamb.com', 'concerts.ical')
    obj.put(Body=ical, ACL='public-read')

    return {
        'status': 200,
    }
