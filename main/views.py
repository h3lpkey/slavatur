from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from slavatur import settings
from urllib.request import urlopen
from .models import Order, OrderSMS

import json
import urllib



def index(request):
	context = {
		'height': True
	}
	return render(request, 'main/index.html', context)


def bus(request):
	context = {
		'1': 1
	}
	return render(request, 'main/module_bus.html', context)


def vizas(request):
	context = {
		'1': 1
	}
	return render(request, 'main/module_vizas.html', context)


def hot(request):
	context = {
		'1': 1
	}
	return render(request, 'main/module_hot.html', context)


def days(request):
	context = {
		'1': 1
	}
	return render(request, 'main/module_days.html', context)


def plane(request):
	context = {
		'1': 1
	}
	return render(request, 'main/module_plane.html', context)


def help(request):
	context = {
		'1': 1
	}
	return render(request, 'main/help.html', context)

def tur(request):
	context = {
		'1': 1
	}
	return render(request, 'main/module_tur.html', context)


def podbor_tura(request):
	context = {
		'1': 1
	}
	return render(request, 'main/module_podbor_tura.html', context)


def contacts(request):
	context = {
		'1': 1
	}
	return render(request, 'main/contacts.html', context)


def about(request):
	context = {
		'1': 1
	}
	return render(request, 'main/about.html', context)


def order(request):
	name = request.POST.get('name', None)
	tel = request.POST.get('tel', None)
	email = request.POST.get('email', None)
	message = request.POST.get('message', None)
	recaptcha_response = request.POST.get('g-recaptcha-response', None)
	context = {}

	if recaptcha_response:
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode("utf-8")
		req = urllib.request.Request(url)
		with urllib.request.urlopen(req, data=data) as f:
			resp = f.read()
			resp = resp.decode()
		result = json.loads(resp)

		# if captcha is valid verifing all the rest
		if all([name, tel, email, message]):
			order = Order(name=name, tel=tel, email=email, message=message)
			order.save()

			context = {
				'order': order
			}

			return render(request, 'main/module_tur.html', context)

		if not result['success']:
			return JsonResponse({'success': 'Каптча на пройдена'})
	else:
		return render(request, 'feedback/index.html', context)


def sms_order(request):
	name = request.POST.get('name', None)
	tel = request.POST.get('tel', None)
	recaptcha_response = request.POST.get('g-recaptcha-response', None)
	context = {}

	if recaptcha_response:
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode("utf-8")
		req = urllib.request.Request(url)
		with urllib.request.urlopen(req, data=data) as f:
			resp = f.read()
			resp = resp.decode()
		result = json.loads(resp)

		# if captcha is valid verifing all the rest
		if all([name, tel]):
			order_sms = OrderSMS(name=name, tel=tel)
			order_sms.save()

			context = {
				'order_sms': order_sms
			}

			return render(request, 'main/module_tur.html', context)

		if not result['success']:
			return JsonResponse({'success': 'Каптча на пройдена'})
	else:
		return render(request, 'feedback/index.html', context)




