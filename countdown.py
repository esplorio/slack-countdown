#!/usr/bin/python
from flask.ext.script import Manager
from flask import Flask
from datetime import datetime
import requests
import json

app = Flask(__name__)
# configure your app

manager = Manager(app)

def daysFromChristmas():
    currentdate = datetime.now()
    christmas = datetime(datetime.today().year,12,25)
    if christmas < currentdate:
        christmas = date(datetime.today().year + 1,12,25)
    delta = christmas - currentdate
    days = delta.days
    return "%d from the nearest Christmas" % days

def daysFromDate(strdate):
    currentdate = datetime.today()
    futuredate = datetime.strptime(strdate, '%Y-%m-%d')
    delta = futuredate - currentdate
    return delta.days
    
def events(strdate,event):
    days = daysFromDate(strdate)
    return "%d days until %s" % (days,event)

def deadline(strdate):
    days = daysFromDate(strdate)
    futuredate = datetime.strptime(strdate, '%Y-%m-%d')
    return "%d days until %s" % (days, futuredate.strftime("%d %B, %Y"))

def post(out):
    url = "https://hooks.slack.com/services/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"
    payload = {'text' : out }
    r = requests.post(url, data=json.dumps(payload))
    


@manager.option("-d", "--deadline", dest="date",
                      help="Specify the deadline in ISO format: yyyy-mm-dd", metavar="DEADLINE")
@manager.option("-e", "--event", dest="event", 
                      help="Name of the deadline event",metavar="EVENT")
def deadline(date,event):
    result = ""
    if date:
        if event:
            result = events(date,event)
        else:
            result = deadline(date)
    else:
        result = daysFromChristmas()
    
    post(result)

    
if __name__ == "__main__":
    manager.run()


