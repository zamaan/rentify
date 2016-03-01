from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from .models import *
from userprofile.forms import ContactForm

# Create your views here.

def home(request):
     return render(request, 'home.html', {
    })


def about(request):
        return render(request,'about.html',{
        })


def contact(request):
    form_class=ContactForm
    if request.method == 'POST':
        form=form_class(data=request.POST)
        if form.is_valid():
                contact_name=form.cleaned_data['contact_name']
                contact_email=form.cleaned_data['contact_email']
                form_content=form.cleaned_data['content']
                template=get_template('contact_template.txt')

                context=Context({
                    'contact_name':contact_name,
                    'contact_email':contact_email,
                    'form_content':form_content,
                    })
                context=template.render(context)
                email=EmailMessage('New contact form submission',content, 'Your website <hi@rental.com>',['zamaan06@gmail.com'],
                    headers= {'Reply-To':contact_email })
                email.send()
                return redirect('contact')
    return render(request,'contact.html',{'form':form_class})

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


def show_profile(request,username=False):
	if username:
		user = User.objects.get(username = username)
		profile = user.profile_set.get()
	else:
		user = request.user
		profile = user.profile_set.get()
	return render_to_response('show_profile.html',
                          {'profile':profile},
                          context_instance=RequestContext(request))

def edit_profile(request):
    # grab the object...
    profile = request.user.profile_set.get()

    # set the form we're using...
    form_class = ProfileForm

    # if we're coming to this view from a submitted form,  
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=profile)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('/profile/')

    # otherwise just create the form
    else:
        form = form_class(instance=profile)

    # and render the template
    return render(request, 'edit_profile.html', {
        'profile': profile,
        'form': form,
    })
