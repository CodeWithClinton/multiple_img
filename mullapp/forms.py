from django import forms
from django.forms import ModelForm
from .models import Image, Product

class ProductForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Product's name"}))
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Product's description"}))
    price = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Product's price"}))
    class Meta:
        model = Product
        exclude = ['vendor']


class ImageForm(ModelForm):
    images = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "multiple":True}))
    class Meta:
        model = Image
        fields = ['images']
    