Countdown program to Slack hook
-------------------------------
Recieve notifications daily about an incoming deadline.

## Setup

There are two ways of setting up. One is to clone this repositry and make any optional modifications to the coundown.py file and deploy it youself to Heroku. The other is to follow
the simple steps below which uses the Heroku button to deploy the app.

1. Create a slack incoming webhook

1. Press this button to create a new Heroku app:

    <a href="https://heroku.com/deploy" target="_blank">
        <img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy">
    </a>

1. Paste the unique URL into the 'SLACK_URL' field and deploy the app.

1. After deployment, click manage apps. You should also get a message to your Slack channel
	to confirm connection.

1. Click on the Heroku Scheduler to set the how often we run the script

1. We will need run the countdown.py deadline task