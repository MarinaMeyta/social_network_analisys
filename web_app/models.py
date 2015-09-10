from django.db import models

# Create your models here.
class Tweets(models.Model):
	tweet_id = models.BigIntegerField(primary_key = True)
	tweet_text = models.CharField(max_length = 140)
	hashtags = models.TextField()
	created_at = models.TextField()
	user_name = models.TextField()
	lang = models.TextField()
	time_zone = models.TextField()
	location = models.TextField()