from django.http import HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
    about_me_list = AboutMe.objects.all()
    banner = Banner.objects.last() or Banner(text="Placeholder, change me")
    context = {
        "about_me_list": about_me_list,
        "banner": banner,
    }
    return render(request, "mathatx/index.html", context)

def IndexView(request):
    template_name = "mathatx/index.html"
