from django import forms
from django.forms import ModelForm
from models import *

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
      #  exclude = ("votos","usuario",)
        