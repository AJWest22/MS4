from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ A view that renders the basket's contents page """

    return render(request, 'basket/basket.html')