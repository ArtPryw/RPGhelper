from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Hero
from .forms import HeroCreateForm
#CRUD methods:

def hero_detail_list_view(request):
    #can listout object
    qs = Hero.objects.all() #.filter() zamiast all() może prawdopodobnie wybierać bohaterów danego użytkownika
    template_name='heroCreator/list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)

def hero_detail_create_view(request):
    #creating by form
    form = HeroCreateForm(request.POST or None)
    if form.is_valid():
        obj = Hero.objects.create(**form.cleaned_data)
        form = HeroCreateForm()
    template_name='form.html'
    context = {'form':form}
    return render(request, template_name, context)


def hero_detail_retrieve_view(request, slug):
    #return one object
    obj = get_object_or_404(Hero, slug=slug)
    template_name='heroCreator/retrieve.html'
    context={"object":obj}
    return render(request, template_name, context)


def hero_detail_update_view(request, slug):
    obj = get_object_or_404(Hero, slug=slug)
    template_name='heroCreator/update.html'
    context={"object":obj, 'form':None}
    return render(request,template_name,context)


def hero_detail_delete_view(request, slug):
    obj = get_object_or_404(Hero, slug=slug)
    template_name='heroCreator/delete.html'
    context={"object":obj}
    return render(request, template_name, context)
