import tweepy

consumer_key = "OUbN0hOILkmGloZue1WglHEdQ"
consumer_secret = "uc37EPwzBJDMQ4qYuDyGIK9cb2akIdu9dStT0A0ktK9VqKedmF"
access_key = '2554976100-Q1ONNkc8GMTpjazcf5lmBQnLtEQMaqjvpCVUXVS'
access_secret = 'XuCHcJvFzqTBEWq095BiaFY9VcH779Bx8ruBoHIQDjyV9'
 
# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
  
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
  
import sys
import jsonpickle
import os
 
searchQuery = '#Putin' or '#Ukrain'
maxTweets = 100000000000
tweetsPerQry = 100
fName = 'tweets.txt'
 
 
# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None
# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1
 
tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,max_id=str(max_id - 1),since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +'\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break
 
print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))