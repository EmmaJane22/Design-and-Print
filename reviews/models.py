from django.db import models
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here


class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='reviews')
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    title = models.CharField(max_length=254)
    review_body = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id
