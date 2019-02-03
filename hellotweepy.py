import tweepy
CONSUMER_KEY = "CVFmG4DSOvGc1gVHtBP5qbYzJ"
CONSUMER_SECRET = "t4ouGgBMNGbabfrSRe7k0rZUVdTIDGNYa7tqL4bEeoEYKitE2u"
ACCESS_TOKEN = "1091439390541271040-otarsi1XOiPZU5vw5L8yqkkNo0NX12"
ACCESS_TOKEN_SECRET = "nq41iqJPyrAHhqywycDn4HpYqLnSta2i412LsHBNjFSVk"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API (auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
