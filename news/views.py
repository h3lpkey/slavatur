from django.shortcuts import render
from django.http import HttpResponse
from .models import News



def index(request):
	news = News.objects.all().order_by('pub_date')
	context = {
		'news': news
	}
	return render(request, 'news/index.html', context)
