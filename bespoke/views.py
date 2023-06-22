from django.shortcuts import render
from .models import BespokeOrder
from django.contrib import messages
from django.conf import settings

def bespoke_products(request):
    """ View to return Bespoke Order page """

    return render(request, 'bespoke/bespoke.html')