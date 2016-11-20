from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from tweets.models import Spam
from tweets.forms import SpamForm

@login_required
def index(request):
	users = User.objects.all()
	tweets = Spam.objects.all()
	username = request.user.username
	full_name = "{} {}".format(request.user.first_name.title(), request.user.last_name.title())
	form = SpamForm()

	context = {
		"username": username,
		"full_name": full_name,
		"users": users,
		"tweets": tweets,
		"form":form,
	}

	return render(request, "core/index.html", context)
