from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Hero

obj = Hero.objects.get(id=1)


def hero_detail_page(request, hero_id):

    obj = get_object_or_404(Hero, id=hero_id)
    template_name = 'hero_detail_page.html'
    context = {"object":obj}
    return render(request,template_name,context)
