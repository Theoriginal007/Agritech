from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello, welcome to my webpage!")
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')
from django.shortcuts import render
