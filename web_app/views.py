#!/usr/bin/python
# -*- coding: utf8 -*-

from django.shortcuts import render, render_to_response, RequestContext ,loader,HttpResponse
from .models import Tweets
import forms
import tweepy
import time
import sqlite3


def home(request):
	latest_question_list = Tweets.objects.all()
	template = loader.get_template('index.html')
	context = RequestContext(request, {'latest_question_list': latest_question_list,})
	return HttpResponse(template.render(context))

def search(request):
		form = {}
		errors=[]
		if request.method=='POST':
			form['tag'] = request.POST.get('tag')
			if not form['tag']:
				errors.append('Errors')
			consumer_key = 'OUbN0hOILkmGloZue1WglHEdQ'
			consumer_secret = 'uc37EPwzBJDMQ4qYuDyGIK9cb2akIdu9dStT0A0ktK9VqKedmF'
			access_token = '1545853322-YL8N6URUxoTQ47LHI8sYnOQA8NoS42bwEYOX46w'
			access_token_secret = 'WFoJ8UirQpk0UWxlSzjUwWKHSBJcs1KFuaX2e1W25frxS'
			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth)
			results = api.search(q = form['tag'], count = 100)
			
			for result in results:
				hash_list=[]
				hash_str=""
				for hashtags in result.entities['hashtags']:
					hash_list.append(hashtags['text'])
					hash_str= ",".join(hash_list)
				q = Tweets(tweet_id=result.id_str,tweet_text=result.text,hashtags=hash_str,created_at=str(result.created_at),user_name=result.user.name,lang=result.user.lang,time_zone=str(result.user.time_zone),location=result.user.location)
				q.save()
		return(home(request))