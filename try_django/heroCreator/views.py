from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import Hero
from .forms import HeroCreateForm, HeroCreateModelForm
#CRUD methods:

def hero_detail_list_view(request):
    #can listout object
    qs = Hero.objects.all() #.filter() zamiast all() może prawdopodobnie wybierać bohaterów danego użytkownika
    template_name='heroCreator/list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)

#@login_required
@staff_member_required
def hero_detail_create_view(request):
    #creating by form
    form = HeroCreateModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.slug = str.lower(form.cleaned_data.get('name') + "-" + form.cleaned_data.get('nickname'))
        obj.user = request.user
        obj.save()
        form = HeroCreateModelForm()
    template_name='form.html'
    context = {'form':form}
    return render(request, template_name, context)


def hero_detail_retrieve_view(request, slug):
    #return one object
    obj = get_object_or_404(Hero, slug=slug)
    template_name='heroCreator/retrieve.html'
    context={"object":obj}
    return render(request, template_name, context)

staff_member_required
def hero_detail_update_view(request, slug):
    obj = get_object_or_404(Hero, slug=slug)
    form = HeroCreateModelForm(request.POST or None, instance=obj)
    template_name='form.html'
    if form.is_valid():
        form.save()
    context={'name':f"Update {obj.name}", "form":form}
    return render(request,template_name,context)

staff_member_required
def hero_detail_delete_view(request, slug):
    obj = get_object_or_404(Hero, slug=slug)
    template_name='heroCreator/delete.html'
    if request.method == "POST":
        obj.delete()
    form = HeroCreateModelForm()
    context={"object":obj}
    return render(request, template_name, context)
