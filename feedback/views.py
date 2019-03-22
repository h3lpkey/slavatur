from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from slavatur import settings
from .models import Comment
import json
import urllib

def index(request):
	comments = Comment.objects.filter(view=True)

	context = {
		'comments': comments
	}
	return render(request, 'feedback/index.html', context)

def post_comment(request):
	email = request.POST.get('email', None)
	comment_text = request.POST.get('comment', None)
	fio = request.POST.get('fio', None)
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
		if all([email, comment_text, fio]):
			comment = Comment(email=email, comment_text=comment_text, fio=fio)
			comment.save()

			context = {
				'comment': comment
			}

			return render(request, 'feedback/index.html', context)

		if not result['success']:
			return JsonResponse({'success': 'Каптча на пройдена'})
	else:
		return render(request, 'feedback/index.html', context)
