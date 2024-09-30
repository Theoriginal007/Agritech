# myproject/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Agritech Project!</h1>")

def signup_view(request):
    return HttpResponse("<h1>Signup Page</h1>")

def item_list_view(request):
    return render(request, 'marketplace/item_list.html')
def item_list(request):
   
    return render(request, 'myapp/item_list.html')
