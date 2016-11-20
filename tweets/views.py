from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Spam
from .forms import SpamForm
from django.contrib.auth.models import User
from user_profiles.models import UserProfile

def tweet_display(request):
	tweets = Spam.objects.all()
	users = User.objects.all()
	profiles = UserProfile()
	form = SpamForm()

	context = {
		"tweets": tweets,
		"users": users,
		"profiles":profiles,
		"form":form,
	}

	return render(request, "tweets/tweet_display.html", context)

def tweet_list(request):
	tweets = Spam.objects.all()
	users = User.objects.all()
	profiles = UserProfile()


	context = {
		"tweets": tweets,
		"users": users,
		"profiles":profiles,

	}

	return render(request, "tweets/tweet_list.html", context)


def tweet_new(request):
	profiles = UserProfile()

	if request.method == "POST":
		form = SpamForm(request.POST)
		if form.is_valid():
			text = form.save(commit=False)
			text.user = request.user
			text.profile = profiles.id

			text.save()
			messages.success(request, "Your Spam has been Posted to the Board!!!")

			return redirect("tweets:tweet_display")

	else:
		form = SpamForm()

	context = {
		"form": form,
	}

	return render(request, "tweets/tweet_new.html", context)
