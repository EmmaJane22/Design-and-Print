from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .models import Review

def all_reviews(request):
    """ View to return all reviews in date order """

    reviews = Review.objects.all()
    reviews.order_by('created_on')
    
    context = {
        'reviews': reviews
    }

    return render(request, 'reviews/reviews.html', context)