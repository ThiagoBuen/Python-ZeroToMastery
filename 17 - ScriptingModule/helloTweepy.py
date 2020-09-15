#Work with Twitter API - tweepy

import tweepy

consumer_key = '128osajkfb82123'                #Generated at twitter dev
consumer_secret = 'hisabjad1239731824hja'
access_token = 'uijknsd91234uiasnkl'
access_token_secret = 'alhskdg18231h1l23'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

print(user)
print(user.screen_name)
print(user.followers_count)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)