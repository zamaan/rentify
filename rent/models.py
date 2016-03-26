#from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

DURATION = (  
    (1, '1 week'),
    (2, '2 weeks'),
    (3, '3 weeks'),
    (4, '1 month'),
)

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

class RequestItem(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)
    duration = models.IntegerField(max_length=50, choices=DURATION)
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s - %s"%(self.item.name,self.user.username)

    def get_rental_price(self):
        return self.item.price * self.duration