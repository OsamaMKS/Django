from django import forms
from django.contrib.auth.models import User
from .models import List, ListItems


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        exclude = ['owner',]

class ItemForm(forms.ModelForm):
    class Meta:
        model = ListItems
        exclude = ['list',]


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
