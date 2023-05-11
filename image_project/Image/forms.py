from django import forms
from .models import ImageEnhance


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageEnhance
        fields = ['title','image']