import uuid

from django.db import models
from products.models import Category
from django.conf import settings

# Create your models here.

class BespokeOrder(models.Model):
    bespoke_order_number = models.CharField(max_length=32, null=True, editable=False)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    description = models.TextField()
    colour = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    quote = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    accept_quote = models.BooleanField(default=False, null=True, blank=True)

    def _generate_bespoke_order_number(self):
        """
        Generate a random unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.bespoke_order_number:
            self.bespoke_order_number = self._generate_bespoke_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bespoke_order_number