"""rentify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from userprofile.views import add_profile, show_profile, edit_profile, home2, home, about, contact, MyRegistrationView
from rent.views import item_detail, item_list, add_item, edit_item, requestitem, requests, change_request_status, request_success

urlpatterns = [
    url(r'^$', home2),
    url(r'^home', home),
    url(r'^about',about),
    url(r'^contact',contact),
    url(r'^admin/', admin.site.urls),
    url(r'^items/',item_list),
    url(r'^item/add/',add_item),
    url(r'^item/(?P<slug>[-\w]+)/$',item_detail), 
    url(r'^item/(?P<slug>[-\w]+)/edit/',edit_item),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/add/',add_profile),
    url(r'^profile/edit',edit_profile),
    url(r'^profile/(\w+)',show_profile),
    url(r'^profile/',show_profile),
    url(r'^requestitem/',requestitem),
    url(r'^request/success/(\d+)/',request_success),
    url(r'^requests/',requests),
    url(r'^request-status/(\d+)/(\w+)/',change_request_status),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)