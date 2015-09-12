
import random
import time
import requests
import tweepy

def randomTimes(averagesecondsbetweencalls):
    print(random.gauss(averagesecondsbetweencalls, 60*1))
    return random.gauss(averagesecondsbetweencalls, 60*1)

#check all of followers
#if they have a star or a retweet, also retweet and/or star

access_token = "1177228129-b5TiIHYD9KlAHNKezwSTm55aWcJpjJSTkzWIrr7"
access_token_secret = "NN8MpxPlFIJiq2ve60rhxdVkix8gWwCtSNdxhHx6Vh8Nc"
consumer_key = "QJfjc4n7I8mheKuHhaCLY7PyD"
consumer_secret = "G1mKQSbVaFm55YSImGDnx2VFBwL7hkWpWmW8NYpGtl9d7iJoPe"



def initTweepy():
    global the_api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    the_api = tweepy.API(auth)


#creates a array 
def getFriends():
    print("getFriends")
    global friendlist
    friendlist = the_api.followers_ids(id = "jakegosskuehn")
    return the_api.followers_ids(id = "jakegosskuehn")

#retweets a tweet
def retweetATweet(tweet_id):
    the_api.retweet(tweet_id)

#creates a favorite for a tweet
def createFavorite(tweet_id):
    ithe_api.create_favorite(tweet_id)

#use tweet.favorited boolean
#   tweet.retweeted boolean
#tweet.id is ID of the tweet, to avoid repeats
def getFavorites(user_id):
    initTweepy

#Gets all of the followers of the authoritating user
#Then gets their public tweets, and checks
    #if its favorited or RT'd, user will do the same.
    #then sleep for 3 min
def checkFriendTimelines():
    for friend_id in friendlist:
        isthetweetspecial = False   
        public_tweets = the_api.user_timeline(id = friend_id )
        for tweet in public_tweets:
            try:
                if tweet.favorited is True:
                    isthetweetspecial = True
                    print("Favored")
                    createFavorite(tweet.id)
       
                if tweet.retweeted is True:
                    isthetweetspecial = True
                    print("RT")
                    tetweetATweet(tweet.id)
                if isthetweetspecial:
                    print(tweet.text)
            except UnicodeEncodeError as e:
                print ("encode error", e)
                
        print("Did one person, now sleeping")
        print(the_api.get_user(friend_id).screen_name)
        time.sleep(180)  

def checkSpecificTweet():
    print(the_api.me)
    public_tweets = the_api.user_timeline()
    for tweet in public_tweets:
        print (tweet.id)
        print (tweet.text)
        print (tweet.favorited)
        time.sleep(10)

initTweepy()
getFriends()
checkSpecificTweet()


###checkFriendTimelines()


