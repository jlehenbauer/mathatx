from django.conf import settings
from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail
from django import forms
import logging

logger = logging.getLogger("views_logger")

def index(request):
    contact_form = contact(request)
    about_me_list = AboutMe.objects.all()
    banner = Banner.objects.last() or Banner(text="Placeholder, change me")
    services = Service.objects.all()
    reviews = Review.objects.all()
    context = {
        "about_me_list": about_me_list,
        "banner": banner,
        "services": services,
        "reviews": reviews,
        "contact_form": contact_form,
    }
    return render(request, "mathatx/index.html", context)

def IndexView(request):
    template_name = "mathatx/index.html"

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        name = form.cleaned_data['name']
        sliding_scale = "yes" if form.cleaned_data['info_sliding_scale'] else "no"
        multiple_students = "yes" if form.cleaned_data['info_multiple_students'] else "no"
        virtual = "yes" if form.cleaned_data['info_virtual_services'] else "no"
        message = "Reply to: " + form.cleaned_data['email'] + "\n\n" + form.cleaned_data['message'] + " \n\n" + "Sliding scale? " + sliding_scale + "\n" + "Multiple students? " + multiple_students + "\n" + "Virtual? " + virtual
        #if form.is_valid():
            #Send email
        if send_mail("New website contact from " + name, message, form.cleaned_data['email'], [settings.EMAIL_HOST_USER]) > 0:
            #return redirect('success')
            form = ContactForm()
        return form
    return ContactForm()
