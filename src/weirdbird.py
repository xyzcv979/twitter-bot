# weirdbird.py
#
# This twitter bot tweets out the weather everyday. Exciting!
#
# Created by Alex Ng
# 07/10/21
import time
import tweepy
import config
import requests
import schedule
import geocoder
import sys

# Authenticate to twitter
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

# OpenWeather API
weather_key = config.WEATHER_KEY
weather_api_link = 'http://api.openweathermap.org/data/2.5/weather?'
# TODO
# dynamic city variable instead of static
g = geocoder.ip('me')  # geocoder used to grab current location
lat = "lat=" + str(g.latlng[0])
lng = "&lon=" + str(g.latlng[1])
city = 'q=New York City'
appID = '&appid=' + weather_key
units = '&units=' + 'imperial'

# Create tweepy API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    sys.exit("ERROR during tweepy authentication")

# Weather variables
# url = weather_api_link + city + appID + units
url = weather_api_link + lat + lng + appID + units
response = requests.get(url)

def tweet():
    if response.status_code == 200:
        print("Weather API request OK\n")
        weather_data = response.json()
        current_temp = weather_data['main']['temp']
        minimum_temp = weather_data['main']['temp_min']
        maximum_temp = weather_data['main']['temp_max']
        humidity = weather_data['main']['humidity']
        weather_desc = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        curr_city = weather_data['name']

        msg = ("Coo Coo!\n" + "Your current location is: " + curr_city + " with " + weather_desc +
               "\ncurrent temp: " + str(int(current_temp)) + "°F, minimum temp: "
               + str(int(minimum_temp)) + "°F, maxmimum temp: " + str(int(maximum_temp))
               + "°F" + "\nhumidity: " + str(int(humidity)) + "% with wind speeds of "
               + str(int(wind_speed)) + "mph" + "\n\n#" + curr_city.replace(" ", "") + " #" +
               curr_city.replace(" ", "") + "Weather")
        # print(msg)
        api.update_status(tweet)
    else:
        print("ERROR during weather API request")

    return schedule.CancelJob


schedule.every().day.at("09:00").do(tweet)
# checks if scheduled task is pending to run or not
while True:
    schedule.run_pending()
    if not schedule.jobs:
        break
    time.sleep(1)

# Create a tweet
# api.update_status("Tweet Tweet!")

# Update profile desc
# api.update_profile(description="I like python")


# TODO
# Run twitter bot off of server
# Package bot using Docker

# TODO
# Run docker image off of amazon aws
