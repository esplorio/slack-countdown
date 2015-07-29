#!/usr/bin/python
from flask.ext.script import Manager
from flask import Flask
from datetime import datetime
import json
import os
import requests

app = Flask(__name__)


manager = Manager(app)

"""Creates web app to be deployed on Heroku."""

SLACK_URL = os.environ.get('SLACK_URL')
if not SLACK_URL:
    print("Missing environment variable SLACK_URL")
    exit(1)


def days_from_christmas():
    """Calculates the number of days between the current date and the next 
    Christmas. Returns the string to displayed.
    """
    currentdate = datetime.now()
    christmas = datetime(datetime.today().year, 12, 25)
    if christmas < currentdate:
        christmas = date(datetime.today().year + 1, 12, 25)
    delta = christmas - currentdate
    days = delta.days
    return "%d from the nearest Christmas" % days


def days_from_date(strdate):
    """ Returns the number of days between strdate and today."""
    currentdate = datetime.today()
    futuredate = datetime.strptime(strdate, '%Y-%m-%d')
    delta = futuredate - currentdate
    return delta.days

    
def events(strdate,event):
    """ Returns string to be displayed with the event mentioned"""
    days = days_from_date(strdate)
    return "%d days until %s" % (days,event)


def deadline(strdate):
    """ Returns string to be displayed"""
    days = days_from_date(strdate)
    futuredate = datetime.strptime(strdate, '%Y-%m-%d')
    return "%d days until %s" % (days, futuredate.strftime("%d %B, %Y"))


def post(out):
    """ Posts a request to the slack webhook. Payload can be customized
    so the message in slack is customized. The variable out is the text 
    to be displayed.
    """    
    
    #url = ("https://hooks.slack.com/services/T02HE4CM9/B0891AYE9/mMTVLFQB5O9ZxWD"
    #      "WUB20Ioej")
    payload = {
        "attachments": [
            {
                "text": out,
                "image_url": "https://tctechcrunch2011.files.wordpress.com/"
                              "2015/01/disruptsf2015_banner.png",
                "color": "#7CD197"
            }
        ]
    }
    
    r = requests.post(SLACK_URL, data=json.dumps(payload))
 

@manager.option("-d", "--deadline", dest="date",
                      help="Specify the deadline in ISO format: yyyy-mm-dd", 
                      metavar="DEADLINE")
@manager.option("-e", "--event", dest="event", 
                      help="Name of the deadline event",metavar="EVENT")
def deadline(date,event):
    """ Method takes two optional arguments. Displays in slack channel
    the number of days till the event. If no arguments are given,
    the number of days till Christmas is displayed.
    """
    result = ""
    if date:
        if event:
            result = events(date, event)
        else:
            result = deadline(date)
    else:
        result = days_from_christmas()
    
    post(result)


@manager.command
def initiate():
    payload = { text: "App is now connected to your Slack Channel."}
    r = requests.post(SLACK_URL, data=json.dumps(payload))
    
    

    
if __name__ == "__main__":
    manager.run()


