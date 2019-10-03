from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
	my_title = 'Hello There...'
	return render(request, "home_page.html", {"title":my_title})

def heroes_page(request):
	return render(request, "heroes_page.html", {"title":"Bohaterowie"})

def game_page(request):
	return render(request, "form.html", {"title":"Rozgrywka"})
