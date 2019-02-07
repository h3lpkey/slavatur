from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main.models import Comment
from slavatur import settings
from urllib.request import urlopen

import json
import urllib



def index(request):
	context = {
		'1': 1
	}
	return render(request, 'main/index.html', context)



def contacts(request):
    return HttpResponse("Contacts.")


def about(request):
    return HttpResponse("About.")


def post_comment(request):
	email = request.POST.get('email', None)
	comment_text = request.POST.get('comment', None)
	credentials = request.POST.get('credentials', None)
	recaptcha_response = request.POST.get('g-recaptcha-response', None)

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
		if all([email, comment_text, credentials]):
			comment = Comment(email=email, comment_text=comment_text, credentials=credentials)
			comment.save()

			return JsonResponse({'success': True})

		if not result['success']:
			return JsonResponse({'success': 'Каптча на пройдена'})
	else:
		return JsonResponse({'success': False })
	
