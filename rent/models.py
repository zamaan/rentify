#from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Item(models.Model):
	name=models.CharField(max_length=255, null=True)
	description=models.TextField(null=True)
	price=models.IntegerField(null=True)
	location=models.CharField(max_length=100,null=True)
	slug=models.SlugField(unique=True,null=True)


def __unicode__(self):
    return self.name

def get_image_path(instance,filename):
	return '/'.join(['item_images', instance.item.slug,filename])

class Upload(models.Model):
	item=models.ForeignKey(Item,related_name="uploads")
	image=models.ImageField(upload_to=get_image_path)
