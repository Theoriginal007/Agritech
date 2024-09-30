# myproject/urls.py

from django.contrib import admin
from django.urls import path
from .views import home, signup_view, item_list_view  # Import the new view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page URL
    path('signup/', signup_view, name='signup'),  # Signup page URL
    path('items/', item_list_view, name='item_list'),  # URL for item list
]
