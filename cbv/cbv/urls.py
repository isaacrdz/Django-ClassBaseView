from django.conf.urls import patterns, include, url
from products.views import ProductDetailView, ProductListView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'products.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'ProductList', name='product_list'),
    url(r'^products/(?P<slug>[\w\-\W]+)', ProductDetailView.as_view()),
    url(r'^products/$', ProductListView.as_view(), name='product'),
    url(r'^add/$', 'products.views.add', name='add'),
   
    url(r'^contacto/$', 'products.views.contacto', name='contacto'),
    url(r'^gracias/$', 'products.views.gracias', name='gracias'),
    url(r'^contactomail/$', 'products.views.contactomail', name='contactomail'),
   


  

 
    
  

    url(r'^admin/', include(admin.site.urls)),
)
