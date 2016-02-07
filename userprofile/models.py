from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.ForeignKey(User)
	full_name = models.CharField(max_length=255)
	age = models.CharField(max_length=100)
	city = models.CharField(max_length=200)
	address = models.TextField()
	bio = models.TextField(blank=True,null=True)

