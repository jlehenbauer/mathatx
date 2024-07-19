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
        print(f"Message sending from {form.cleaned_data['name']} and email {form.cleaned_data['email']}: {form.cleaned_data['message']} \n\n" +
                    f"Sliding scale? {form.cleaned_data['info_sliding_scale']}\n" +
                    f"Multiple students? {form.cleaned_data['info_multiple_students']}\n" +
                    f"Virtual? {form.cleaned_data['info_virtual_services']}")
        message = (f"{form.cleaned_data['message']} \n\n" +
            f"Sliding scale? {"yes" if form.cleaned_data['info_sliding_scale'] else "no"}\n" +
            f"Multiple students? {"yes" if form.cleaned_data['info_multiple_students'] else "no"}\n" +
            f"Virtual? {"yes" if form.cleaned_data['info_virtual_services'] else "no"}")
        #if form.is_valid():
            #Send email
        if send_mail(f"New website contact from {form.cleaned_data['name']}", message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER]) > 0:
            #return redirect('success')
            form = ContactForm()
        return form
    return ContactForm()