from django.shortcuts import render, render_to_response, RequestContext ,loader,HttpResponse
from .models import Tweets

# Create your views here.

def home(request):
	latest_question_list = Tweets.objects.order_by('-tweet_text')[:5]
	template = loader.get_template('web_app/index.html')
	context = RequestContext(request, {'latest_question_list': latest_question_list,})
	return HttpResponse(template.render(context))