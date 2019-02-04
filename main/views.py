from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Main app.")


def contacts(request):
    return HttpResponse("Contacts.")


def about(request):
    return HttpResponse("About.")