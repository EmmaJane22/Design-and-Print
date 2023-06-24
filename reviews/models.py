from django.db import models
from profiles.models import UserProfile

# Create your models here

class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='reviews')
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    title = models.CharField(max_length=254)
    review_body = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
