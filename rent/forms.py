from django import forms
from django.forms import ModelForm
from rent.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description','price','location')


