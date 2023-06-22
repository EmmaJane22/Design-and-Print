from django.shortcuts import render
from .models import BespokeOrder

def bespoke_products(request):
    """ View to return Bespoke Order page """

    return render(request, 'bespoke/bespoke.html', context)