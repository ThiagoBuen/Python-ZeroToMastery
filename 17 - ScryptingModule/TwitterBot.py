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


#Narcissistic bot

strSearchKeyword = 'My user name'
numberOfTweets = 5

for tweet in limit_handler(tweepy.Cursor(api.search, strSearchKeyword).items(numberOfTweets)):
    try:
        tweet.favorite()
        tweet.retweet()
        print('I liked and retweeted that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
