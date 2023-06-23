from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import BespokeOrder
from .models import UserProfile

@login_required
def bespoke_orders(request):
    """ View to return Bespoke Order page """
    if request.user.is_superuser:
        bespoke_orders = BespokeOrder.objects.order_by('created_date')
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
        bespoke_orders = profile.bespoke_orders.order_by('created_date')
    
    context = {
        'bespoke_orders': bespoke_orders
    }

    return render(request, 'bespoke/bespoke_orders.html', context)
