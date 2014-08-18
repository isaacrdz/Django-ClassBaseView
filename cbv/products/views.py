# -*- coding: utf-8 -*-
from .models import Product
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.mail import EmailMessage
from forms import *



def home(request):
	template  ='index.html'
	return render(request, template)

class ProductDetailView(DetailView):
	model = Product

	def get_template_names(self):
		return 'products_list.html'



class ProductListView (ListView):
    model = Product
    def get_template_names(self):
        return 'product_list.html'
	product = Product.objectsorder_by("slug").all()





def add(request):
	# if this is a POST request we need to process the form data
	    if request.method == 'POST':
	        # create a form instance and populate it with data from the request:
	        form = ProductForm(request.POST)
	        # check whether it's valid:
	        if form.is_valid():
	            # process the data in form.cleaned_data as required
	            form.save()
	            # redirect to a new URL:
	            return HttpResponseRedirect('/products/')

	    # if a GET (or any other method) we'll create a blank form
	    else:
	        form = ProductForm()
		 

	    return render(request, "form.html", (locals()))


def contacto(request):
	if request.method == 'POST': #Si el formulario es enviado
		form = Formulario(request.POST)
		if form.is_valid(): # Si es valido se procesan los datos ...
			return HttpResponseRedirect('/gracias')

	else:
		form = Formulario()

	return render(request,'contacto.html',{
		 'form':form,
		})

def gracias(request):
	html = '<html><body>Gracias por enviarnos su comentario</body></html>'
	return HttpResponse(html)



def contactomail(request):
	if request.method == 'POST':
		formulario = FormularioContacto(request.POST)
		if formulario.is_valid():
			asunto = 'Este es un mensaje de prueba enviado desde Django'
			mensaje = formulario.cleaned_data['mensaje']
			mail =EmailMessage(asunto,mensaje, to=['zackcpp@gmail.com'] )
			mail.send()
		return HttpResponseRedirect('/')


	else:
		formulario = FormularioContacto()

	return render_to_response('contacto_mail.html',{'formulario': formulario}, context_instance=RequestContext(request))