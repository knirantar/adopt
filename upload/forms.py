from django.forms import ModelForm
from django import forms
from .models import *



class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class ImageForm(ModelForm):
    class Meta:
        model = AnimalImages
        fields = '__all__'