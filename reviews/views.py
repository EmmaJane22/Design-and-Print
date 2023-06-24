from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Review

def all_reviews(request):
    """ View to return all reviews in date order """

    reviews = Review.objects.all()
    reviews.order_by('created_on')
    
    context = {
        'reviews': reviews
    }

    return render(request, 'reviews/reviews.html', context)

@login_required
def delete_review(request, review_id):
    """ Allow admin to delete review """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you don\'t have permission to do that.')
        return redirect(reverse('reviews'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, f'{review.title} deleted')

    return redirect(reverse('reviews'))