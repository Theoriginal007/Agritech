# myapp/tests.py

from django.test import TestCase
from .models import Item

class ItemModelTest(TestCase):
    
    def setUp(self):
        """Create a sample item for testing."""
        Item.objects.create(name='Test Item', price=10.00, description='A test item')

    def test_item_creation(self):
        """Test that the item is created with correct attributes."""
        item = Item.objects.get(name='Test Item')
        self.assertEqual(item.price, 10.00)
        self.assertEqual(item.description, 'A test item')
        self.assertIsNotNone(item.created_at)  # Check that created_at is set
