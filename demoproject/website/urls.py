from django.urls import path
from . import views


urlpatterns = [


    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('darshan/', views.darshan, name="darshan"),
    path('event/', views.event, name="event"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),






]






