Countdown program to Slack hook
-------------------------------

[![Requirements Status](https://requires.io/github/esplorio/slack-countdown/requirements.svg?branch=master)](https://requires.io/github/esplorio/slack-countdown/requirements/?branch=master)
[![Code Climate](https://codeclimate.com/github/esplorio/slack-countdown/badges/gpa.svg)](https://codeclimate.com/github/esplorio/slack-countdown)

Receive notifications daily about an incoming deadline.

## Background

We built this in the run up to TC Disrupt SF 2015 to light a giant fire under our arses.

![tc-disrupt](https://s3-eu-west-1.amazonaws.com/generic-assets.esplor.io/images_on_web/TC_Disrupt_Slack_Countdown_Hook.png)

## Setup

There are two ways of setting up. One is to clone this repository and make any optional modifications to the coundown.py file and deploy it yourself to Heroku. The other is to follow the simple steps below which uses the Heroku button to deploy the app.

A prerequisite is that you have a Heroku account and have added a method of payment on there. Including add ons on a Heroku app, even though the Heroku Scheduler is free, requires that the account has a method of payment.

**NOTE:** If you use the heroku deployment button, you wont be able to upload a picture or other modifications

1. Create a <a href="https://slack.com/services/new/incoming-webhook" target="_blank"> new incoming webhook</a> for your Slack channel and copy the unique URL. This is the URL countdown.py will be sending post requests to.

2. Press this button to create a new Heroku app:

    <a href="https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2Fesplorio%2Fslack-countdown%2Ftree%2Fmaster" target="_blank">
        <img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy">
    </a>

3. When prompted by Heroku, paste the unique URL into the `SLACK_URL` field under `Config variables` and deploy the app.

4. After deployment, click on "manage apps". You should also get a message to your Slack channel
    to confirm connection.

5. Click on the Heroku Scheduler, this will open up a dashboard where we can run scripts periodically.

6. We will need run the countdown.py deadline task. The specification for the method is as follows:
    ```
    The method takes two optional arguments.

    Options:
      -d DEADLINE, --deadline=DEADLINE
                            Specify the deadline in ISO format: yyyy-mm-dd
      -e EVENT, --event=EVENT
                            Name of the deadline event
    ```
    i.e.
    If the date today is the 16th July 2015 then
    - `countdown deadline -d 2015-07-18` will print out “2 days until 18 July 2015”
    - `countdown deadline -d 2015-07-18 -e weekend` will print out “2 days until weekend”.

    If no argument is given, the default is for the method to post how many days till the
    next Christmas.

7. In the terminal type:
    ```
    python countdown.py deadline
    ```
    followed by your desired arguments.

8. Next specify how often you want the script to run, i.e. how often you want a reminder of your deadline in the Slack Channel.

9. Once this is saved the app is complete.
