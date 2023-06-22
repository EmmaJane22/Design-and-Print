from django.db import models
from products.models import Category

# Create your models here.

class BespokeOrder(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    description = models.TextField()
    colour = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    quote = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    accept_quote = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name