from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import Animal,AnimalImages
from .forms import AnimalForm,ImageForm
# Create your views here.
