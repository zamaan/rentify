from django.contrib import admin
#Register your models here.
from rent.models import Item,Upload

class ItemAdmin(admin.ModelAdmin):
	model=Item
	list_display=('name','description','price','location',)
	prepopulated_fields={'slug':('name',)}

class UploadAdmin(admin.ModelAdmin):
	list_display=('item',)
	list_display_links=( 'item',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Upload, UploadAdmin)