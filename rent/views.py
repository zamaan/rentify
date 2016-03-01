from django.shortcuts import render
from rent.models import Item
# Create your views here.

def item_list(request):
	items=Item.objects.all()
	return render(request, 'item_list.html',{
		'items':items,
		})

def item_detail(request,id):
	item=Item.objects.get(pk=id)
	return render(request, 'item_detail.html',{
		'item':item,
		})