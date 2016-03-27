from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from rent.models import Item, RequestItem
from rent.forms import ItemForm
from django.http import HttpResponseRedirect
from rent.utils import send_request_email
# Create your views here.

def item_list(request):
    items=Item.objects.all()
    return render(request, 'item_list.html',{
        'items':items,
        })

def item_detail(request, slug):

    item = Item.objects.get(slug=slug)
    return render(request, 'item_detail.html',{
        'item':item,
        })

@login_required

def add_item(request):
    form_class = ItemForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST,request.FILES)

        if form.is_valid():
            # create an instance but do not save yet
            items = form.save(commit=False)

            # set the additional details
            items.user = request.user
            items.slug = slugify(items.name)

            # save the object
            items.save()

            # redirect to our newly created thing
            return redirect('/profile')

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
        form = form_class(data=request.POST, files=request.FILES, instance=item)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('/item/%s/'%item.slug, slug=item.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=item)

    # and render the template
    return render(request, 'edit_item.html', {
        'item': item,
        'form': form,
    })

def requests(request):
    user = request.user
    requests = []
    user_items = user.item_set.all()
    for item in user_items:
        for i in item.requestitem_set.filter(status="requested"):
            requests.append(i)

    approved_requests = []
    for item in user_items:
        for i in item.requestitem_set.filter(status="approved"):
            approved_requests.append(i)

    fulfilled_requests = []
    for item in user_items:
        for i in item.requestitem_set.filter(status="fulfilled"):
            fulfilled_requests.append(i)
    
    
    return render(request, 'requests.html', {
        'requests': requests,
        'approved_requests': approved_requests,
        'fulfilled_requests': fulfilled_requests,
    })


def requestitem(request):
    if request.method == "POST":
      user = request.user
      item_id = request.POST['item_id']
      item = Item.objects.get(id = item_id)
      duration = request.POST['duration']
      status = "requested"
    
      item_request,created = RequestItem.objects.get_or_create(
                                       user = user, 
                                       item = item, 
                                       duration = duration, 
                                       status = status)
      return redirect('/request/success/%d/'%item_request.id)
    if created:   
        send_request_email(item.user.email,item_request)
    ###send email to item owner that a request has been made by {{user.profile.name}} etc

def request_success(request,r_id):
    r_item = RequestItem.objects.get(id=r_id)
    return render(request, 'request_success.html',{
        'r_item':r_item,
        })

def change_request_status(request,r_id,status):
    request_item = RequestItem.objects.get(id=r_id)
    request_item.status = status
    request_item.save()
    ## send emaul that request has been approved
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))