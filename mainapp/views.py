from django.shortcuts import HttpResponse, HttpResponseRedirect, render

# Create your views here.

from django.urls import reverse
from django.views.defaults import page_not_found

from random import randrange
from .menu import _menu
# Create your views here.

def error_404_view(request, exception):
   
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')

def index(request):
    all_menu = _menu
    context = {
        "menus" : _menu
    }
    return render(request, 'mainapp/index.html',context)

def about(request):
    context = {
        "title": "About Us  ",
        "crumb_to": "Home",
        "link": "index",
        "banner" : "images/banner/bnr1.jpg"
    }
    return render(request, 'mainapp/about-us.html', context)

def faq(request):
    context = {
        "title": "Frequently Asked Questions",
        "crumb_to": "Home",
        "link": "index",
        "banner" : "images/banner/bnr2.jpg"
    }
    return render(request, 'mainapp/faq.html', context)

def team(request):
    context = {
        "title": "Team",
        "crumb_to": "Home",
        "link": "index",
        "banner" : "images/banner/bnr3.jpg"
    }
    return render(request, 'mainapp/team.html', context)

def testimonial(request):
    context = {
        "title": "Testimonials",
        "crumb_to": "Home",
        "link": "index",
        "banner" : "images/banner/bnr5.jpg"
    }
    return render(request, 'mainapp/testimonial.html', context)

def contact(request):
    context = {
        "title": "Contact Us",
        "crumb_to": "Home",
        "link": "index",
        "banner" : "images/banner/bnr1.jpg"
    }
    return render(request, 'mainapp/contact-us.html', context)

def services(request):
    context = {
        "title": "Our Services",
        "crumb_to": "Home",
        "link": "index",
        "banner" : "images/banner/bnr1.jpg"
    }
    return render(request, 'mainapp/services.html', context)

def book(request):
    context = {
        "title": "Our Services",
        "crumb_to": "Home",
        "link": "index",
        "banner" : "images/banner/bnr1.jpg"
    }
    return render(request, 'mainapp/shop-cart.html', context)

# def book_details(request):
#     context = {
#         "title": "Booking Details",
#         "crumb_to": "Home",
#         "link": "index",
#         "banner" : "images/banner/bnr3.jpg"
#     }
#     return render(request, 'mainapp/shop-checkout.html', context)

def menu(request, slug):
    all_menu = _menu

    single_menu = next(
        menu for menu in all_menu if menu['slug'] == slug)
    context = {
        "title": "Booking Details",
        "subtitle": single_menu['title'],
        "crumb_to": "Home",
        "link": "index",
        "single_menu": single_menu,
        "thumbnail":single_menu['image'],
        "banner" : single_menu['image'],
    }
    print(single_menu['image'])
    return render(request, 'mainapp/shop-checkout.html', context)
