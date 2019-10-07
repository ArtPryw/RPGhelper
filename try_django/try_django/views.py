from django.http import HttpResponse
from django.shortcuts import render
from .forms import CharacterForm

def home_page(request):
	my_title = 'Hello There...'
	return render(request, "home_page.html", {"title":my_title})

def heroes_page(request):
	return render(request, "heroes_page.html", {"title":"Bohaterowie"})

def game_page(request):
	form = CharacterForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = CharacterForm()
	context = {
	"title":"Rozgrywka",
	 "form" : form
	}
	return render(request, "form.html", context)
