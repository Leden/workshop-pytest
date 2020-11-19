from django import forms

from . import models

class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = models.ShortUrl
        fields = ['full']
