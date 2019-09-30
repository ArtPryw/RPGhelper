from django.shortcuts import render

# Create your views here.
from .models import Hero

obj = Hero.objects.get(id=1)


def hero_detail_page(request):
    obj = Hero.objects.get(id=1)
    template_name = 'hero_detail_page.html'
    context = {"object":obj}
    return render(request,template_name,context)
