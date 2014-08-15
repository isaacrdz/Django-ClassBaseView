from django.db import models

class Product(models.Model):
	name = models.CharField( max_length=50)
	category = models.CharField(max_length=100)
	content = models.TextField()
  	slug = models.SlugField(max_length=100, blank=True)
	

	def __unicode__(self):
		return self.name
