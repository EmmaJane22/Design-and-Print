from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .models import BespokeOrder
from .forms import BespokeOrderForm, BespokeOrderQuoteForm, BespokeOrderQuoteAcceptForm


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


@login_required
def quote_bespoke_order(request, bespoke_order_id):
    """ Allow admin to add quote price to bespoke order """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you don\'t have permission to do that.')
        return redirect(reverse('home'))

    bespoke_order = get_object_or_404(BespokeOrder, pk=bespoke_order_id)
    if request.method == 'POST':
        form = BespokeOrderQuoteForm(request.POST, instance=bespoke_order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bespoke order updated successfully!')
            return redirect(reverse('bespoke_order_detail', args=[bespoke_order.id]))
        else:
            messages.error(request, 'Failed to update bespoke order. Check the form is valid.')
    else:
        form = BespokeOrderQuoteForm(instance=bespoke_order)
        messages.info(request, f'You are editing {bespoke_order.title}')
    
    template = 'bespoke/quote_bespoke_order.html'
    context = {
        'form': form,
        'bespoke_order': bespoke_order,
    }

    return render(request, template, context)

@login_required
def accept_bespoke_order(request, bespoke_order_id):
    """ Allow user to accept a quote for bespoke order """

    bespoke_order = get_object_or_404(BespokeOrder, pk=bespoke_order_id)
    if request.method == 'POST':
        form = BespokeOrderQuoteAcceptForm(request.POST, instance=bespoke_order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quote accepted!')
            return redirect(reverse('bespoke_order_detail', args=[bespoke_order_id]))
        else:
            messages.error(request, 'Failed to update bespoke order. Check the form is valid.')
    else:
        form = BespokeOrderQuoteAcceptForm(instance=bespoke_order)
        messages.info(request, f'You are editing {bespoke_order.title}')
    
    template = 'bespoke/accept_bespoke_order.html'
    context = {
        'form': form,
        'bespoke_order': bespoke_order,
    }

    return render(request, template, context)