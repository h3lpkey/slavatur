from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context = {
		'1': 1
	}
	return render(request, 'main/index.html', context)



def contacts(request):
    return HttpResponse("Contacts.")


def about(request):
    return HttpResponse("About.")