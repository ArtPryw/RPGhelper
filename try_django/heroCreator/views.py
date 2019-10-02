from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Hero

#CRUD methods:

def hero_detail_list_view(request):
    #can listout object
    qs = Hero.objects.all() #.filter() zamiast all() może prawdopodobnie wybierać bohaterów danego użytkownika
    template_name='hero_detail_list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)

def hero_detail_create_view(request):
    #creating by form
    template_name='hero_detail_create.html'
    context = {'form':None}
    return render(request, template_name, context)


def hero_detail_retrieve_view(request, slug):
    #return one object
    obj = get_object_or_404(Hero, slug=slug)
    template_name='hero_detail_retrieve.html'
    context={"object":obj}
    return render(request, template_name, context)


def hero_detail_update_view(request, slug):
    obj = get_object_or_404(Hero, slug=slug)
    template_name='hero_detail_update.html'
    context={"object":obj, 'form':None}
    return render(request,template_name,context)


def hero_detail_delete_view(request, slug):
    obj = get_object_or_404(Hero, slug=slug)
    template_name='hero_detail_delete.html'
    context={"object":obj}
    return render(request, template_name, context)
