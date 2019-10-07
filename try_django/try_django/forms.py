from django import forms


class CharacterForm(forms.Form):
    name   = forms.CharField()
    email       = forms.EmailField()
    content = forms.CharField(widget = forms.Textarea)
