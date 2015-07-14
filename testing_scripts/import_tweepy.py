#!/usr/bin/python
# -*- coding: utf8 -*-

import tweepy
import sqlite3

# данные для OAuth-соединения
consumer_key =  'L4ujZnSzxiMCqY6nC6TMiSAgO'
consumer_secret = 'kuKFKNyNHFY8hJSaW4Y8rgKfNY9an2v0V66ie5M8y0VsBD15dn'
access_token = '2554976100-Q1ONNkc8GMTpjazcf5lmBQnLtEQMaqjvpCVUXVS'
access_token_secret = 'XuCHcJvFzqTBEWq095BiaFY9VcH779Bx8ruBoHIQDjyV9'

# авторизуемся на сервере и выводим в консоль ленту твитов 
# собственного аккаунта
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

temp_list = []
public_tweets = api.home_timeline()
for tweet in public_tweets:
    #print tweet.text
    temp_list.append(tweet.text)

for x in temp_list:
	print(x)

# создаем (открываем ранее созданную) БД и курсор для работы с ней
con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS tweets (id INTEGER PRIMARY KEY NOT NULL, tweet VARCHAR(140), mood VARCHAR(3))')
con.commit()


insert_str = "INSERT INTO tweets (id, tweet, mood) VALUES(?, ?, 'pos')"

id_counter = 0
for x in temp_list:
	data = (id_counter, x)
	cur.execute(insert_str, data)
	id_counter += 1
	
con.commit()
#print cur.lastrowid

cur.execute('SELECT * FROM tweets')
#print cur.fetchall()
con.close()