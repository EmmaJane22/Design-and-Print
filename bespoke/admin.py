from django.contrib import admin
from .models import BespokeOrder

# Register your models here.
class BespokeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'description',
        'colour',
        'image',
        'quote',
        'accept_quote',
    )

    ordering = ('title',)

admin.site.register(BespokeOrder, BespokeAdmin)