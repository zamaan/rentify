from django.shortcuts import render
from rent.models import Item
# Create your views here.

def item_detail(request):
	items=Item.objects.all()
	return render(request, 'item_detail.html',{
		'items':items,
		})