from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    email = forms.CharField(min_length=1, widget=forms.EmailInput, label=_("Email"))
    password = forms.CharField(min_length=1, widget=forms.PasswordInput, label=_("Password"))