# myapp/views.py

from django.shortcuts import render, get_object_or_404
from .models import Item

def item_list(request):
    """Display a list of items."""
    items = Item.objects.all()  # Get all items from the database
    return render(request, 'myapp/item_list.html', {'items': items})  # Render the template

def item_detail(request, item_id):
    """Display details for a specific item."""
    item = get_object_or_404(Item, id=item_id)  # Fetch the item or return a 404 if not found
    return render(request, 'myapp/item_detail.html', {'item': item})  # Render the item detail template
