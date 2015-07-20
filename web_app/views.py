#!/usr/bin/python
# -*- coding: utf8 -*-

from django.shortcuts import render, render_to_response, RequestContext ,loader,HttpResponse
from .models import Tweets
import tweepy
import time
import sqlite3


def home(request):
	consumer_key = 'OUbN0hOILkmGloZue1WglHEdQ'
	consumer_secret = 'uc37EPwzBJDMQ4qYuDyGIK9cb2akIdu9dStT0A0ktK9VqKedmF'
	access_token = '1545853322-YL8N6URUxoTQ47LHI8sYnOQA8NoS42bwEYOX46w'
	access_token_secret = 'WFoJ8UirQpk0UWxlSzjUwWKHSBJcs1KFuaX2e1W25frxS'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	results = api.search(q = "#ведьмак" or 'ведьмак', count = 100)
	for result in results:
			hash_list=[]
			for hashtags in result.entities['hashtags']:
				hash_list.append(hashtags['text'])
				hash_str= ",".join(hash_list)

			q = Tweets(tweet_id=result.id_str,tweet_text=result.text,hashtags=hash_str,created_at=str(result.created_at))
			q.save()

	latest_question_list = Tweets.objects.all()
	template = loader.get_template('web_app/index.html')
	context = RequestContext(request, {'latest_question_list': latest_question_list,})
	return HttpResponse(template.render(context))