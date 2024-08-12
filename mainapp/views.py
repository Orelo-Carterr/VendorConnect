from django.shortcuts import HttpResponse, HttpResponseRedirect, render

# Create your views here.

from django.urls import reverse
from django.views.defaults import page_not_found

from random import randrange

# Create your views here.

def error_404_view(request, exception):
   
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')

def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    context = {
        "title": "About Us  ",
        "crumb_to": "Home",
        "link": "index"
    }
    return render(request, 'mainapp/about-us.html', context)

def faq(request):
    context = {
        "title": "Frequently Asked Questions",
        "crumb_to": "Home",
        "link": "index"
    }
    return render(request, 'mainapp/faq.html', context)

def team(request):
    context = {
        "title": "Team",
        "crumb_to": "Home",
        "link": "index"
    }
    return render(request, 'mainapp/team.html', context)

def testimonial(request):
    context = {
        "title": "Testimonials",
        "crumb_to": "Home",
        "link": "index"
    }
    return render(request, 'mainapp/testimonial.html', context)

def contact(request):
    context = {
        "title": "Contact Us",
        "crumb_to": "Home",
        "link": "index"
    }
    return render(request, 'mainapp/contact-us.html', context)

def services(request):
    context = {
        "title": "Our Services",
        "crumb_to": "Home",
        "link": "index"
    }
    return render(request, 'mainapp/services.html', context)