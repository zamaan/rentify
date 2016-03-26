#from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User)
    name=models.CharField(max_length=255,null=True)
    image=models.ImageField(null=True,blank=True)
    description=models.TextField(null=True)
    price=models.IntegerField(null=True)
    location=models.CharField(max_length=100,null=True)
    slug=models.SlugField(unique=True,null=True)

    def __unicode__(self):
        return self.name

def get_image_path(instance,filename):
	return '/'.join(['item_images', instance.item.slug,filename])

def get_absolute_url(self):
    	return "/item/%s/" %self.slug

