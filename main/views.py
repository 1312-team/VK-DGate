from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, "about_us.html")

def index(request):
    return render(request, "index.html")