from django import forms


class UserFrom(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
