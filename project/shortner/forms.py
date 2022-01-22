from dataclasses import field
from django import forms
from .models import Shorturl

class UrlForm(forms.ModelForm):
    class Meta:
        model = Shorturl
        fields = ['long_url']