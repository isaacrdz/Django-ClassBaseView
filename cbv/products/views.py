from .models import Product
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from forms import *



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






