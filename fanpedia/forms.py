from django import forms
from .models import FanPedia

class FanPediaForm(forms.ModelForm):
    class Meta:
        model = FanPedia
        fields = ['title']
        