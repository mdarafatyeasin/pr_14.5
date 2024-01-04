from django.shortcuts import render
from . import forms

# Create your views here.
def home (request) :
    my_form = forms.add_input()
    return render (request, 'home.html', {'form':my_form})