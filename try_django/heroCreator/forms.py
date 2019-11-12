from django import forms
from .models import Hero
import random

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


def statsRandomizer():
    str_random = random.randint(1,20)
    mana_random = random.randint(1,100)
    HP_random = random.randint(1,30)
    result = [str_random, mana_random, HP_random]
    return result

listOfRandomStats = statsRandomizer()



class HeroCreateModelForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['name', 'nickname', 'race', 'profession' ]
        strength    = listOfRandomStats[0]
        mana        = listOfRandomStats[1]
        HP          = listOfRandomStats[2]

    def clean_name(self, *args, **kwargs):
        instance = self.instance
        name = self.cleaned_data.get('name')
        qs = Hero.objects.filter(name__iexact=name) # iexact - lovercase/upper unique check
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) #id = instance Pk = primary key
        if qs.exists():
            raise forms.ValidationError("This name is already exist! Please change it to unique one.")
        return name
