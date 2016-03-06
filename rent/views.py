from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from rent.models import Item
from rent.forms import ItemForm

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

@login_required

def add_item(request):
    form_class = ItemForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)

        if form.is_valid():
            # create an instance but do not save yet
            items = form.save(commit=False)

            # set the additional details
            items.user = request.user
            items.slug = slugify(items.name)

            # save the object
            items.save()

            # redirect to our newly created thing
            return redirect('/items/', slug=items.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'add_item.html', {
        'form': form,
    })
