# myapp/models.py

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)  # Name of the item
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item
    description = models.TextField()  # Description of the item
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the item was created

    def __str__(self):
        return self.name  # Returns the name of the item when the object is printed
