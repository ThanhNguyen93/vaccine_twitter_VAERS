#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:48:32 2019

@author: thanhng
"""
import csv

def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # initialization of a list to hold all Tweets
    all_the_tweets = []
    
    # We will get the tweets with multiple requests of 200 tweets each
    
    new_tweets = api.user_timeline(screen_name=screen_name, count=3200)
    
    # saving the most recent tweets
    
    all_the_tweets.extend(new_tweets)
    
    # save id of 1 less than the oldest tweet
    oldest = all_the_tweets[-1].id - 1
    
    # grabbing tweets till none are left    
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=3200,max_id=oldest)
		
		#save most recent tweets
        all_the_tweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
        oldest = all_the_tweets[-1].id - 1
		
        print("...%s tweets downloaded so far"%(len(all_the_tweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in all_the_tweets]
	
    return outtweets
    
	#write the csv	
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
	
    pass

lt = get_all_tweets("J_tsar")

lt[2]

len(lt)
