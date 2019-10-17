from django import forms


class CharacterForm(forms.Form):
    name   = forms.CharField()
    email       = forms.EmailField()
    content = forms.CharField(widget = forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email.endswith(".edu"):
            raise forms.ValidationError("This is not vaild email. Please, do not use .edu domain")

        return email
