from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('book/', views.book, name='book'),
    path('book-details/<slug:slug>', views.menu, name='book-details'),
    
   
]