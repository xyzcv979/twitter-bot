# weirdbird.py
#
# This twitter bot tweets out the weather everyday. Exciting!
#
# Created by Alex Ng
# 07/10/21

import tweepy
import config

# Authenticate to twitter
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Create a tweet
#api.update_status("Hello tweepy!")

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("ERROR during authentication")


# TODO
# Run twitter bot off of server
# Package bot using Docker

# TODO
# Run docker image off of amazon aws


