from django import forms
from .models import Hero

class HeroCreateForm(forms.Form):

    name        = forms.CharField()
    nickname    = forms.CharField()
    race        = forms.CharField()
    profession  = forms.CharField()

    #To do ogarnięcia bo nie działa.
    slug        = forms.SlugField()

    strength    = forms.IntegerField()
    mana        = forms.IntegerField()
    HP          = forms.IntegerField()

class HeroCreateModelForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['name', 'nickname', 'race', 'profession', 'strength', 'mana', 'HP']

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        qs = Hero.objects.filter(name__iexact=name) # iexact - lovercase/upper unique check
        if qs.exists():
            raise forms.ValidationError("This name is already exist! Please change it to unique one.")
        return name
