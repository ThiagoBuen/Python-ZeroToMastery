#Work with Twitter API - tweepy

import tweepy
import time
consumer_key = '128osajkfb82123'                #Generated at twitter dev
consumer_secret = 'hisabjad1239731824hja'
access_token = 'uijknsd91234uiasnkl'
access_token_secret = 'alhskdg18231h1l23'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(200)


#Generous bot

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.followers_count > 1000:
        follower.follow()
        break

    print(follower.name)
