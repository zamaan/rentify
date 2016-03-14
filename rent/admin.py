from django.contrib import admin
#Register your models here.
from rent.models import Item,Upload

class ItemAdmin(admin.ModelAdmin):
	model=Item
	list_display=('name','description','price','location','image')
	prepopulated_fields={'slug':('name',)}


admin.site.register(Item, ItemAdmin)
