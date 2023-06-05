from django.shortcuts import render

def view_bag(request):
    """ View to render bag contents page """

    return render(request, 'bag/bag.html')