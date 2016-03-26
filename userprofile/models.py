from __future__ import unicode_literals
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Profile(models.Model):
	user = models.ForeignKey(User)
	full_name = models.CharField(max_length=255)
	age = models.CharField(max_length=100)
	city = models.CharField(max_length=200)
	address = models.TextField()
	bio = models.TextField(blank=True,null=True)
	phone_number = models.CharField(max_length=100)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
