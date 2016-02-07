from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def add_profile(request):
    form_class = ProfileForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)

        if form.is_valid():
            # create an instance but do not save yet
            userprofile = form.save(commit=False)

            # set the additional details
            userprofile.user = request.user

            # save the object
            userprofile.save()

            # redirect to our newly created thing
            return redirect('/profile')

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'add_profile.html', {
        'form': form,
    })