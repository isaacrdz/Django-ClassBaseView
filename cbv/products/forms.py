from django import forms
from django.forms import ModelForm
from models import *

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
     	exclude = ("slug",)



class Formulario(forms.Form):
	nombre = forms.CharField(max_length=100)
	mensaje = forms.Field()
	mail = forms.EmailField()


class FormularioContacto(forms.Form):
	correo = forms.EmailField()
	mensaje = forms.CharField()
	
        