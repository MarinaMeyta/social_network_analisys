#!/usr/bin/python
# -*- coding: utf8 -*-

import tweepy
import time
import sqlite3

consumer_key = 'OUbN0hOILkmGloZue1WglHEdQ'
consumer_secret = 'uc37EPwzBJDMQ4qYuDyGIK9cb2akIdu9dStT0A0ktK9VqKedmF'
access_token = '1545853322-YL8N6URUxoTQ47LHI8sYnOQA8NoS42bwEYOX46w'
access_token_secret = 'WFoJ8UirQpk0UWxlSzjUwWKHSBJcs1KFuaX2e1W25frxS'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
results = api.search(q = "#Путин", count = 100)
con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS tweets (tweet_id integer PRIMARY KEY NOT NULL, tweet_text VARCHAR(140),hashtags text,created_at text,user_name text,lang text,time_zone text,location text )')
con.commit()

print "Loading..."

for result in results:
	select_cmd = 'SELECT user_name FROM tweets WHERE tweet_id = ?'
	cur.execute(select_cmd, (result.id_str,))
	if (cur.fetchone() == None):
		# print "***"
		# print "Tweet id: " + result.id_str
		# print "Tweet text: "+result.text
		# print "Retweet count: " + str(result.retweet_count)
		# print "Favorite count: " + str(result.favorite_count)
		# print "Created at: "+ str(result.created_at)
		# print "result place: " + str(result.place)
		# print "Source: " + result.source
		# print "Coordinates: " + str(result.coordinates)
		# print "User name: " + result.user.name
		# print "Description: " + result.user.description
		# print "Language: " + result.user.lang
		# print "Account created at: " + str(result.user.created_at)
		# print "Location: " + result.user.location
		# print "Time zone: " + str(result.user.time_zone)
		# print "Number of tweets: " + str(result.user.statuses_count)
		# print "Number of followers: " + str(result.user.followers_count)
		# print "Following: " + str(result.user.friends_count)
		# print "A member of " + str(result.user.listed_count) + " lists."
		# time.sleep(1)
		hash_list=[]
		for hashtags in result.entities['hashtags']:
			hash_list.append(hashtags['text'])
		hash_str= ",".join(hash_list)
		cur.execute("insert into tweets (tweet_id, tweet_text,hashtags,created_at,user_name,lang,time_zone,location) values(?,?,?,?,?,?,?,?)",(result.id_str,result.text,hash_str,str(result.created_at),result.user.name,result.user.lang, str(result.user.time_zone),result.user.location,))
		con.commit()
