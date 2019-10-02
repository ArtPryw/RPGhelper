from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Hero

def hero_detail_page(request, slug):

    obj = get_object_or_404(Hero, slug=slug)
    template_name = 'hero_detail_page.html'
    context = {"object":obj}
    return render(request,template_name,context)
