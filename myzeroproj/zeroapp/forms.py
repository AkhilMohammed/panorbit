from django import forms
from .models import signup

from django.contrib.auth.base_user import AbstractBaseUser
class Loginform(forms.Form):
    email=forms.EmailField(max_length=30)


class signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields=['firstname','lastname','gender','mobile','email']