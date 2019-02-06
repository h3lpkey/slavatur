from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context = {
		'1': 1
	}
	return render(request, 'news/index.html', context)
