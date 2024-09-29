from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Connects the 'home_view' function from views.py
]
