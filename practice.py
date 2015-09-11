




#try the redditbot here

import random
import time
import praw
import requests
import tweepy

access_token = "1177228129-MjmHpmpOqXvLwdWvBdXJ09xqAIBIM8ecWCrdxO4"
access_token_secret = "vdTOEsKEGIOnAcSadokDLuDQgTEXIU1eUYe6iMjegE9CB"
consumer_key = "OffKgwzpLV4gdTX8uo6YMEteo"
consumer_secret = "N8MBsa8oVMLC29onaN4LVBz08FK2zynHzh1861o0uMp1CpqUmT"

r = praw.Reddit('Test Program to Read Headlines')

r.login('jakeinmn', '638743', disable_warning=True)

def randomTimes(averagesecondsbetweencalls):
    return random.gauss(averagesecondsbetweencalls, 60*3)

def add_id_to_file(theID):
    with open('posted_posts.txt', 'a') as file:
        file.write(str(theID) + "\n")

def duplicate_check(theID):
    found = 0
    with open ('posted_posts.txt', 'r') as file:
        for line in file:
            if theID in line:
                found = 1
    return found

def trunticateTwitterString(title, short_url):
    length = len(title)
    #the URL is how many characters long?
    #117 characters left, save one for a space at end
    if length < 116:
        #if the post is long enough, add the link for credit
        #is this what I should do?

        return title + " " + short_url
    elif length < 140:
        return title
    else:
        print("the title is too long, wat do?")
        return False

def post_to_twitter(text_to_send):
    if text_to_send is False:
        return
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    result = api.update_status(status = text_to_send)
    return result
   # public_tweets = api.home_timeline()
#
   # for tweet in public_tweets:
   #     print(tweet.text)

   


                          
while True:
    subreddit = r.get_subreddit('showerthoughts')
    for submisssion in subreddit.get_top_from_day(limit=10):
        shortlink = submisssion.short_link
        the_id = submisssion.id
        title = submisssion.title
        #op_headline

        

        if duplicate_check(the_id) == 0:
            add_id_to_file(the_id)
            print(title)
            print(shortlink)
            #what to send to twitter:
            texttosend = trunticateTwitterString(title, shortlink)
            if texttosend is False:
                print("too long of a post")
            else:
                post_to_twitter(texttosend)
                print("SUCCESSFUL POST")
        else:
           print('repeated submission')
        time.sleep(randomTimes(60*30))
        
            

        #make sure the title is within the 
        #140 characters for twitter














def singSong():
    countofbeers = 100
    print( "test")
    print( countofbeers)

    for i in range(countofbeers):
        countofbeers_str = str(countofbeers)
        countofbeers_str_minus1 = str(countofbeers - 1)
        print( countofbeers_str + " bottles of beer on the wall")
        print( countofbeers_str + " bottles of beer on the wall")
        print("take one down, pass it around")
        print(countofbeers_str_minus1 + " bottles of beer on the wall")
        countofbeers = countofbeers - 1
        
    
#singSong()

def coinChecker(weightofcoins, coin):
    weightofpennies = 2.5
    weightofnickles = 5
    weightofdimes = 2.268
    weightofquarters = 5.67

    if coin == "penny":
        print("Pennies:")
        print(weightofcoins / weightofpennies)
        print("Penny containers filled:")
        print(weightofcoins / weightofpennies / 100)

#coinChecker(5, "penny")   
        





   
        
