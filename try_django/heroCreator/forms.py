from django import forms

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
