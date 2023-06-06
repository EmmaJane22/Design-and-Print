from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(erquest, "Your bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NG0vZHVk8XuBzHY5JpUOBJkslMzVbQHM7QhNiEZXD3ZoWX4XOrfMpRHHub2063mDEs7ZpTw554dfuWgf9QKH5Pw00k3n12FJ2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
