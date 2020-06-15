import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from tweepy import API

import pandas as pd

import sys
import os


access_token = "2877893220-uPMqt8oOxJJQvX74iRF2vbDmU7fHe3b5BRYOMD0"
access_token_secret = "Bzx70wOYiWfAkZ1BKwywEIJB6lOHxztCYhNoTvnw7moYc"
consumer_key = "i01QqTQTsRC05dJsXmY5mnBN4"
consumer_secret = "d21fWhVfukVIY4y8VJneNltYGVBkd5zq7yDm1BWTgCYR38miMv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth, wait_on_rate_limit=True)

#################
#read keywords
text = open("health_keywords.txt", "r")

line = text.read()      # Read the line in as before
singles = line.split(',\n')

first_half = singles[:len(singles)//6]

keyword_first = " OR ".join([str(x) for x in first_half])  

keyword_first

keywords = " OR ".join([str(x) for x in singles])  

keywords

keywords + 'influenza' + ' -filter:retweets' 

###############

len(keywords)

#########
query = "flu vaccine OR flu shot OR flushot OR influenza OR #flushot OR #fluvaccine -filter:retweets"

query = 'covid19 vaccine OR covid-19 vaccine OR covid19 vaccines'
tweets = tweepy.Cursor(api.search,
                       q=query,
                       lang="en",
                       since="2020-02-01", 
                       until = '2020-06-05').items()
#
count = 0
for tweet in tweets:
   count +=1
   # printing the text stored inside the tweet object
   print ('user:', tweet.user.screen_name, '\n',
          'USER ID: ', tweet.user.id_str, '\n', 
          'tweetID:', tweet.id_str, '\n',
          'created_at:', tweet.created_at, '\n', 
          'location:', tweet.user.location, '\n',
          "Tweeted:",tweet.text, '\n')
   
print("Downloaded {0} tweets".format(count))
    
 #####
###iterate over cursor

user_ID = []
tweet_ID = []
tweet_date = []
content = []  
location = [] 

tweetCount = 0
for tweet in tweepy.Cursor(api.search,
                               q=query, 
                               lang="en").items(): 
    user_ID.append(tweet.user.id_str)
    tweet_ID.append(tweet.id_str)
    tweet_date.append(tweet.created_at)
    content.append(tweet.text) 
    location.append(tweet.user.location)
    
    tweetCount += 1

print("Downloaded {0} tweets".format(tweetCount))
         
   
############
#add to cols

d = {'created_at': tweet_date, 'user_ID':user_ID,'tweet_ID': tweet_ID,  
    'content': content}

df = pd.DataFrame(d)

df.to_csv('tweets.csv')
    

###################
for tweet in tweets:
    print(tweet.text, '\n')
    
#date
for tweet in tweets:
    print(tweet.created_at, '\n')    
    
 #tweet ID
for tweet in tweets:
    print(tweet._json['id'], '\n')       
###########################  
    

    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
  
class StdOutListener(tweepy.StreamListener):
    def on_status(self, status):
        
        print(status.text)
        return True
   
    def on_error(self, status_code):
        if status_code == 420:
            return False
    
tweetcounts =0
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    tweets = stream.filter(track=['flushot', '#flushot', 'flu vaccine', 'flu shot', 'influenza'], 
                                  languages=["en"])
  #  print(tweets.text)
    
    if 'RT @' not in tweets.text: 
  #  if (not tweets.retweeted) and ('RT @' not in tweets.text):
        try:                                  
            for tw in tweets:
                tweetcounts +=1
        except Exception as e:
                # Print the error
            print(e)
            # and continue
            pass
            
print("Downloaded {0} tweets".format(tweetCount))
         
    
    
##############
#multiple search
 query = ['medstar', 'flu vaccine', 'flu shot', 'influenza']

results = api.search(q='flu vaccine', lang='en') + api.search(q='influenza', lang='en')

################## 
l = StdOutListener()

# Create a stream object with listener and authorization
stream = Stream(auth, l)

# Run the stream object using the user defined queries
stream.filter(track=['medstar', 'flu vaccine', 'flu shot', 'influenza'])   

############
item = api.get_user(24247194)
print("name: " + item.name)
print("screen_name: " + item.screen_name)
print("description: " + item.description)
print("statuses_count: " + str(item.statuses_count))
print("friends_count: " + str(item.friends_count))
print("followers_count: " + str(item.followers_count))


print(item.geo_enabled)
 