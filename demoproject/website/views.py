from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,"web/index.html")

def about(req):
    return render(req,"web/about.html")

def darshan(req):
    return render(req,"web/darshan.html")

def event(req):
    return render(req,"web/event.html")

def gallery(req):
    return render(req,"web/gallery.html")

def contact(req):
    return render(req,"web/contact.html")