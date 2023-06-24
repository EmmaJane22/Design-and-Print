from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'rating',
        'title',
        'review_body',
        'created_on',
    )

admin.site.register(Review, ReviewAdmin)
