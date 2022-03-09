import gspread
from twitter import *


consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''

gc = gspread.service_account('credentials.json')
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# open the relevant google sheet 
wks = gc.open("twitter-bot").sheet1

# update with the new tweet
next_tweet = wks.acell('A2').value

# post tweet through twitter api
t.statuses.update(
    status=next_tweet)

# delete row once tweet is sent
wks.delete_rows(2)
