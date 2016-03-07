from django import forms
from django.forms import ModelForm
from rent.models import Item,Upload

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description','price','location')

class UploadForm(ModelForm):
	class Meta:
		model=Upload
		fields=('image')
