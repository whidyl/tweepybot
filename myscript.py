import tweepy
from datamuse import datamuse
from random import randint
NAME = "@BeepBoo62501238"
CONSUMER_KEY = "CVFmG4DSOvGc1gVHtBP5qbYzJ"
CONSUMER_SECRET = "t4ouGgBMNGbabfrSRe7k0rZUVdTIDGNYa7tqL4bEeoEYKitE2u"
ACCESS_TOKEN = "1091439390541271040-otarsi1XOiPZU5vw5L8yqkkNo0NX12"
ACCESS_TOKEN_SECRET = "nq41iqJPyrAHhqywycDn4HpYqLnSta2i412LsHBNjFSVk"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API (auth)
api2 = datamuse.Datamuse()

# generate list of rhymes for specifiec word
def getRhymes(str) : 
    rhymes = api2.words(rel_rhy=str, max = 50)
    return(rhymes)

# randomly returns a rhyme datamuse list of rhymes
def getRandomRhyme(r):
    randIndex = randint(0,len(r)-1)
    rhyme = r[randIndex]
    response = rhyme.get('word')
    return response

# create a stream that processes any tweets that contain the word "haiku"
# each processed tweet will have each word in it's text converted into similar rhymes
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print("----------------NEW TWEET---------------- ")
        print(status.text)

        # convert status.text into a string of similar rhymed words
        words = status.text.split(' ')
        rhymedWords = words
        for i in range(len(words)):
            rhymes = getRhymes(words[i])
            try:
                rhymedWords[i] = getRandomRhyme(rhymes)
            except:
                rhymedWords[i] = words[i]
        print("----------------  RHYMED  ---------------")
        print(' '.join(rhymedWords))

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=["haiku"])

