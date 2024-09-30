from django.contrib import admin
from django.urls import path, include  # Import include
from . import views
from .views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include URLs from your app
    path('myapp/', include('myapp.urls')),  # Include your app's URLs
   path('', home, name='home'),  # This is where 'home' is used
]

from . import views

urlpatterns = [
    # Other URL patterns...
    path('signup/', views.signup_view, name='signup'),  # Make sure this exists
]

