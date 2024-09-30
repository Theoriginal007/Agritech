# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),  # Map the root URL to the item_list view
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),  # URL for item details
]
