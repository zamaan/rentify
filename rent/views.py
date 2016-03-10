from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from rent.models import Item, Upload
from rent.forms import ItemForm, UploadForm

# Create your views here.

def item_list(request):
	items=Item.objects.all()
	return render(request, 'item_list.html',{
		'items':items,
		})

def item_detail(request, slug):

	item = Item.objects.get(slug=slug)
	uploads=item.uploads.all()
	return render(request, 'item_detail.html',{
		'item':item,
		'uploads':uploads
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

def edit_item(request, slug):
    # grab the object...
    item = Item.objects.get(slug=slug)

    # grab the current logged in user and make sure they're the owner of the thing
    #if item.user != request.user:
     #   raise Http404

    # set the form we're using...
    form_class = ItemForm

    # if we're coming to this view from a submitted form,  
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=item)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('/items/', slug=item.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=item)

    # and render the template
    return render(request, 'edit_item.html', {
        'item': item,
        'form': form,
    })

def add_photo(request, slug):
	item=Item.objects.get(slug=slug)
	#if thing.user != request.user:
	#	raise Http404
	form_class = UploadForm
	if request.method == 'POST':
		form=form_class(data=request.POST, files=request.FILES, instance=thing)
			
	if form.is_valid():
	
		Upload.objects.create(image=form.cleaned_data['image'],thing=thing,)
		return redirect('item_detail', slug=thing.slug)
	
	else:
		form=form_class(instance=item)
		uploads=items.uploads.all()

	return render(request, '/item/add/photo/',{
					'items':items,
					'form':form,
					'uploads':uploads,
	}
	)
