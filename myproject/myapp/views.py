from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def item_list(request):
    """Display a list of items."""
    items = Item.objects.all()  # Get all items from the database
    # If items have a rating, create a range for display (assuming `rating` is an integer field in your model)
    for item in items:
        item.rating_range = range(item.rating)  # Create a rating range for display
    return render(request, 'myapp/item_list.html', {'items': items})  # Render the template

def item_detail(request, item_id):
    """Display details for a specific item."""
    item = get_object_or_404(Item, id=item_id)  # Fetch the item or return a 404 if not found
    return render(request, 'myapp/item_detail.html', {'item': item})  # Render the item detail template

def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page or dashboard
    else:
        form = AuthenticationForm()  # Initialize an empty form
    return render(request, 'myapp/login.html', {'form': form})  # Render the login template


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to a login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})
from django.shortcuts import render

def item_list(request):
    # Rendering the correct template
    return render(request, 'myapp/item_list.html')
