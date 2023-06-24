from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .models import BespokeOrder
from .forms import BespokeOrderForm


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


@login_required
def bespoke_order_detail(request, bespoke_order_id):
    """ View to show bespoke order details """

    bespoke_order = get_object_or_404(BespokeOrder, pk=bespoke_order_id)

    context = {
        'bespoke_order': bespoke_order,
    }

    return render(request, 'bespoke/bespoke_order_detail.html', context)

@login_required
def add_bespoke_order(request):
    """ Create bespoke order """
    if request.method == "POST":
        print('if post = true')
        form = BespokeOrderForm(request.POST, request.FILES)
        if form.is_valid():
            bespoke_order = form.save()
            messages.success(request, 'Bespoke order added successfully')
            return redirect(reverse('bespoke')) #, args=[bespoke_order.bespoke_order_number]))
        else:
            messages.error(request, 'Failed to add bespoke order.')
    else:
        form = BespokeOrderForm()

    template = 'bespoke/add_bespoke_order.html'
    context = {
        'form': form,
    }

    return render(request, template, context)