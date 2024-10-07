from django import forms
from .models import Product
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'volume', 'image']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return strip_tags(name)
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        return strip_tags(description)