from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "index.html", context={'value': "lunch"})


def user_page(request, user_name):
    return HttpResponse(f"<h1>{user_name}</h1>")
