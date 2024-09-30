# myapp/admin.py

from django.contrib import admin
from .models import Item  # Import the Item model

# Register your models with the Django admin
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at')  # Columns to display
    search_fields = ('name',)  # Enable search by item name
