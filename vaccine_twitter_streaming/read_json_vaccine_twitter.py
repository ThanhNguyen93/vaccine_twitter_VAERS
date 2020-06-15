#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:12:05 2019

@author: thanhng
"""

import json

    
tweets = []
for line in open('vaccine_sentiment.json', 'r'):
    tweets.append(json.loads(line)) 
    
tweets = []
for line in open('flu_vaccine_new.json', 'r'):
    tweets.append(json.loads(line))   
    

type(tweets[2])

tweets[2].items

for key, val in tweets[20].items():
   print (key, val, '\n')

tweet_dict = tweets[5].get('tweet')

tweet_dict

tweet_dict.get('text')


data = '{"tweet": {"lang": "en", "favorited": false, "in_reply_to_user_id": null, "contributors": null, "truncated": false, "text": "i get my flu shot on December 21st A FLU SHOT AINT GON SAVE ME FROM THE APOCALYPSE MUTHAFUCKA", "created_at": "Sun Dec 09 01:39:22 +0000 2012", "retweeted": false, "in_reply_to_status_id": null, "coordinates": null, "id": 277588214733230080, "entities": {"user_mentions": [], "hashtags": [], "urls": []}, "in_reply_to_status_id_str": null, "id_str": "277588214733230080", "in_reply_to_screen_name": null, "user": {"follow_request_sent": null, "profile_use_background_image": true, "id": 35623916, "verified": false, "profile_image_url_https": "https://si0.twimg.com/profile_images/2946385109/fd4b74f0a6423bddfdd570bfcf9cbff6_normal.jpeg", "profile_sidebar_fill_color": "D11E1E", "is_translator": false, "geo_enabled": false, "profile_text_color": "F000D0", "followers_count": 59, "protected": false, "location": "", "default_profile_image": false, "id_str": "35623916", "utc_offset": -21600, "statuses_count": 140, "description": "niall took a shit on my bio", "friends_count": 21, "profile_link_color": "0084B4", "profile_image_url": "http://a0.twimg.com/profile_images/2946385109/fd4b74f0a6423bddfdd570bfcf9cbff6_normal.jpeg", "notifications": null, "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/728446933/f9b68edaa8d38d7be1ef5d9786dd3255.jpeg", "profile_background_color": "00F7D2", "profile_banner_url": "https://si0.twimg.com/profile_banners/35623916/1354579453", "profile_background_image_url": "http://a0.twimg.com/profile_background_images/728446933/f9b68edaa8d38d7be1ef5d9786dd3255.jpeg", "screen_name": "harryfeels_no", "lang": "en", "profile_background_tile": true, "favourites_count": 20, "name": "meganigga", "url": "", "created_at": "Mon Apr 27 01:13:45 +0000 2009", "contributors_enabled": false, "time_zone": "Central Time (US & Canada)", "profile_sidebar_border_color": "FFFFFF", "default_profile": false, "following": null, "listed_count": 0}, "place": null, "retweet_count": 0, "geo": null, "in_reply_to_user_id_str": null, "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>"}, "id": "277588214733230080", "label": {"flu_vaccine_received": "received", "flu_vaccine_sentiment": "neutral", "flu_vaccine_relevant": "yes", "flu_vaccine_intent_to_receive": "yes"}}'

json.dumps(data, indent = 4)