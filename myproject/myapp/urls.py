# myapp/urls.py

from django.urls import path
from . import views
from .views import signup_view
urlpatterns = [
    path('', views.item_list, name='item_list'),  # Map the root URL to the item_list view
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),  # URL for item details
]

from django.urls import path
from .views import item_list, login_view  # Import your views

urlpatterns = [
    path('', item_list, name='home'),  # Update as needed
    path('login/', login_view, name='login'),  # Add this line
]

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    # Other URL patterns...
]
# urls.py
from django.urls import path
from . import views  # Make sure this imports the correct views file

urlpatterns = [
    path('items/', views.item_list, name='item_list'),  # Add this line for item list
]
from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.item_list, name='item_list'),  # URL route for the item list
]
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),  # URL for signup page
    path('items/', views.item_list, name='item_list'),  # URL for item list
]
