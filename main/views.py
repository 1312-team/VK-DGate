from django.shortcuts import render
from django.http.response import HttpResponse
from main.actions import *
# Create your views here.

def about(request):
    return render(request, "about_us.html")

def index(request):
    return render(request, "index.html")

def go_subscribe(request):
    token = 'PASTE UR TOKEN RIGHT HERE (with access rights to user\'s groups)'
    group_id = '22822305'
    result = subscribe_to_group(group_id, token)
    if result:
        pass
    return HttpResponse(result)
